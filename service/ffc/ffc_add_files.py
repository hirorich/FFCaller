# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import pathlib, shutil
from common import app_property
from common.utility import file_utils, log_utils, path_utils
from service.analyzer import analyzer_ffprobe
from service.ffc.sql import ffc_add_files_sql, ffc_insert
from service.ffc.entity.target_entity import TargetEntity
from service.ffc.entity.trim_entity import TrimEntity
from service.ffc.entity.file_entity import FileEntity
from service.ffc.entity.format_entity import FormatEntity
from service.ffc.entity.stream_entity import StreamEntity
from service.ffc.entity.video_entity import VideoEntity
from service.ffc.entity.audio_entity import AudioEntity

# 実行
def exec(conn):
    try:
        # 作業フォルダ作成
        workdir = pathlib.Path(path_utils.convert_to_absolute_path(app_property.eel.init)).joinpath(app_property.workdir)
        workdir.mkdir(exist_ok=True)
        
        # 対象ファイル選択
        for input_file in file_utils.open_file_dialog():
            
            # 対象ファイル追加
            file_duration_entity = __add_file(workdir, conn, input_file)
            
            # トリム情報DB登録
            __insert_triminfo(conn, file_duration_entity)
            
    except Exception as e:
        message = log_utils.write_exception(e)

# 対象ファイル追加
def __add_file(workdir, conn, input_file):
    
    file_entity = FileEntity()
    
    # ファイル情報取得
    file = pathlib.Path(input_file)
    file_entity.filename = file.name
    file_entity.filepath = file.resolve().absolute().as_posix()
    
    # 登録済み情報取得
    file_duration_entity = ffc_add_files_sql.get_file_duration_by_path(conn, file_entity.filepath)
    if file_duration_entity.file_id is not None:
        return file_duration_entity
    
    # ファイルID発行
    file_entity.file_id = ffc_add_files_sql.get_max_file_id(conn) + 1
    
    # ファイルコピー
    copiedfile = str(file_entity.file_id) + file.suffix
    file_entity.workpath = workdir.joinpath(copiedfile).as_posix()
    file_entity.webpath = pathlib.Path(app_property.workdir).joinpath(copiedfile).as_posix()
    shutil.copy(file_entity.filepath, file_entity.workpath)
    
    # ファイル解析(ffprobe)
    analized_result = analyzer_ffprobe.analize(file_entity.workpath)
    
    # ファイル情報DB追加
    return __insert_fileinfo(conn, file_entity, analized_result)

# ファイル情報DB追加
def __insert_fileinfo(conn, file_entity, analized_result):
    
    # Fileテーブル追加
    ffc_insert.insert_file(conn, file_entity)
    
    # Formatテーブル追加
    format_entity = FormatEntity()
    format_entity.file_id = file_entity.file_id
    format_entity.nb_streams = analized_result['format']['nb_streams']
    format_entity.duration = analized_result['format']['duration']
    format_entity.size = analized_result['format']['size']
    ffc_insert.insert_format(conn, format_entity)
    
    # ストリーム情報追加
    for stream in analized_result['streams']:
        
        # Streamテーブル追加
        stream_entity = StreamEntity()
        stream_entity.file_id = file_entity.file_id
        stream_entity.stream_index = stream['index']
        stream_entity.codec_type = stream['codec_type']
        stream_entity.codec_name = stream['codec_name']
        stream_entity.codec_long_name = stream['codec_long_name']
        stream_entity.duration = stream['duration']
        stream_entity.bit_rate = stream['bit_rate']
        ffc_insert.insert_stream(conn, stream_entity)
        
        if (stream_entity.codec_type == 'video'):
            
            # Videoテーブル追加
            video_entity = VideoEntity()
            video_entity.file_id = stream_entity.file_id
            video_entity.stream_index = stream_entity.stream_index
            video_entity.width = stream['width']
            video_entity.height = stream['height']
            video_entity.r_frame_rate = stream['r_frame_rate']
            video_entity.nb_frames = stream['nb_frames']
            ffc_insert.insert_video(conn, video_entity)
            
        elif (stream_entity.codec_type == 'audio'):
            
            # Audioテーブル追加
            audio_entity = AudioEntity()
            audio_entity.file_id = stream_entity.file_id
            audio_entity.stream_index = stream_entity.stream_index
            audio_entity.sample_rate = stream['sample_rate']
            ffc_insert.insert_audio(conn, audio_entity)
    
    # 登録情報返却
    return ffc_add_files_sql.get_file_duration_by_id(conn, file_entity.file_id)

# トリム情報DB追加
def __insert_triminfo(conn, file_duration_entity):
    
    # Targetテーブル登録
    target_entity = TargetEntity()
    target_entity.target_id = ffc_add_files_sql.get_max_target_id(conn) + 1
    target_entity.file_id = file_duration_entity.file_id
    target_entity.item_order = ffc_add_files_sql.get_max_item_order(conn) + 1
    ffc_insert.insert_target(conn, target_entity)
    
    # Trimテーブル登録
    trim_entity = TrimEntity()
    trim_entity.target_id = target_entity.target_id
    trim_entity.trim_duration = file_duration_entity.trim_duration
    trim_entity.end_frame = file_duration_entity.nb_frames
    ffc_insert.insert_trim(conn, trim_entity)
