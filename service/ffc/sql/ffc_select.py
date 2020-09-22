# ==================================================
# ffc_dbの情報取得
# ==================================================

from common.utility import sqlite3_utils
from service.ffc.entity.audio_entity import AudioEntity
from service.ffc.entity.file_entity import FileEntity
from service.ffc.entity.format_entity import FormatEntity
from service.ffc.entity.stream_entity import StreamEntity
from service.ffc.entity.target_entity import TargetEntity
from service.ffc.entity.trim_entity import TrimEntity
from service.ffc.entity.video_entity import VideoEntity
from service.ffc.entity.work_input_target_entity import InputTargetEntity
from service.ffc.entity.work_audio_stream_entity import AudioStreamEntity
from service.ffc.entity.work_video_stream_entity import VideoStreamEntity

# 入力ターゲットリスト取得
def get_input_target_list(conn):
    query = []
    query.append(r'select')
    query.append(r'Target.target_id, File.filename, File.filepath, Trim.start_time, Trim.end_time, Target.item_order')
    query.append(r'from Target')
    query.append(r'inner join Trim')
    query.append(r'on Target.target_id = Trim.target_id')
    query.append(r'inner join File')
    query.append(r'on Target.file_id = File.file_id')
    query.append(r'order by')
    query.append(r'Target.item_order, Target.target_id')
    
    result = []
    for input_target in sqlite3_utils.fetchall(conn, ' '.join(query)):
        entity = InputTargetEntity()
        entity.target_id = input_target[0]
        entity.filename = input_target[1]
        entity.filepath = input_target[2]
        entity.start_time = input_target[3]
        entity.end_time = input_target[4]
        entity.item_order = input_target[5]
        result.append(entity)
    
    return result

# ターゲット取得
def get_target(conn, target_id):
    query = []
    query.append(r'select')
    query.append(r'target_id, file_id, item_order')
    query.append(r'from Target')
    query.append(r'where')
    query.append(r'target_id = ?')
    query.append(r'order by')
    query.append(r'target_id')
    param = (target_id,)
    
    target = sqlite3_utils.fetchone(conn, ' '.join(query), param)
    if target is None:
        return None
    
    target_entity = TargetEntity()
    target_entity.target_id = target[0]
    target_entity.file_id = target[1]
    target_entity.item_order = target[2]
    
    return target_entity

# トリム取得
def get_trim(conn, target_id):
    query = []
    query.append(r'select')
    query.append(r'target_id, start_time, end_time, start_frame, end_frame, frame_input_flag, video_fade_in, video_fade_out, audio_fade_in, audio_fade_out')
    query.append(r'from Trim')
    query.append(r'where')
    query.append(r'target_id = ?')
    query.append(r'order by')
    query.append(r'target_id')
    param = (target_id,)
    
    trim = sqlite3_utils.fetchone(conn, ' '.join(query), param)
    if trim is None:
        return None
    
    trim_entity = TrimEntity()
    trim_entity.target_id = trim[0]
    trim_entity.start_time = trim[1]
    trim_entity.end_time = trim[2]
    trim_entity.start_frame = trim[3]
    trim_entity.end_frame = trim[4]
    trim_entity.frame_input_flag = trim[5]
    trim_entity.video_fade_in = trim[6]
    trim_entity.video_fade_out = trim[7]
    trim_entity.audio_fade_in = trim[8]
    trim_entity.audio_fade_out = trim[9]
    
    return trim_entity

# ファイル取得
def get_file(conn, file_id):
    query = []
    query.append(r'select')
    query.append(r'file_id, filename, filepath, workpath, webpath')
    query.append(r'from File')
    query.append(r'where')
    query.append(r'file_id = ?')
    query.append(r'order by')
    query.append(r'file_id')
    param = (file_id,)
    
    file = sqlite3_utils.fetchone(conn, ' '.join(query), param)
    if file is None:
        return None
    
    file_entity = FileEntity()
    file_entity.file_id = file[0]
    file_entity.filename = file[1]
    file_entity.filepath = file[2]
    file_entity.workpath = file[3]
    file_entity.webpath = file[4]
    
    return file_entity

# フォーマット取得
def get_format(conn, file_id):
    query = []
    query.append(r'select')
    query.append(r'file_id, nb_streams, duration, size')
    query.append(r'from Format')
    query.append(r'where')
    query.append(r'file_id = ?')
    query.append(r'order by')
    query.append(r'file_id')
    param = (file_id,)
    
    format = sqlite3_utils.fetchone(conn, ' '.join(query), param)
    if format is None:
        return None
    
    format_entity = FormatEntity()
    format_entity.file_id = format[0]
    format_entity.nb_streams = format[1]
    format_entity.duration = format[2]
    format_entity.size = format[3]
    
    return format_entity

# 映像ストリーム取得
def get_video_stream(conn, file_id):
    query = []
    query.append(r'select')
    query.append(r'Stream.file_id, Stream.stream_index, ')
    query.append(r'Stream.codec_type, Stream.codec_name, Stream.codec_long_name, Stream.duration, Stream.bit_rate, ')
    query.append(r'Video.width, Video.height, Video.r_frame_rate, Video.nb_frames')
    query.append(r'from Stream')
    query.append(r'inner join Video')
    query.append(r'on Stream.file_id = Video.file_id')
    query.append(r'and Stream.stream_index = Video.stream_index')
    query.append(r'where')
    query.append(r'Stream.file_id = ?')
    query.append(r'order by')
    query.append(r'Stream.file_id, Stream.stream_index')
    param = (file_id,)
    
    video_stream = sqlite3_utils.fetchone(conn, ' '.join(query), param)
    if video_stream is None:
        return None
    
    stream_entity = StreamEntity()
    stream_entity.file_id = video_stream[0]
    stream_entity.stream_index = video_stream[1]
    stream_entity.codec_type = video_stream[2]
    stream_entity.codec_name = video_stream[3]
    stream_entity.codec_long_name = video_stream[4]
    stream_entity.duration = video_stream[5]
    stream_entity.bit_rate = video_stream[6]
    
    video_entity = VideoEntity()
    video_entity.file_id = video_stream[0]
    video_entity.stream_index = video_stream[1]
    video_entity.width = video_stream[7]
    video_entity.height = video_stream[8]
    video_entity.r_frame_rate = video_stream[9]
    video_entity.nb_frames = video_stream[10]
    
    video_stream_entity = VideoStreamEntity()
    video_stream_entity.stream = stream_entity
    video_stream_entity.video = video_entity
    
    return video_stream_entity

# 音声ストリーム取得
def get_audio_streams(conn, file_id):
    query = []
    query.append(r'select')
    query.append(r'Stream.file_id, Stream.stream_index, ')
    query.append(r'Stream.codec_type, Stream.codec_name, Stream.codec_long_name, Stream.duration, Stream.bit_rate, ')
    query.append(r'Audio.sample_rate')
    query.append(r'from Stream')
    query.append(r'inner join Audio')
    query.append(r'on Stream.file_id = Audio.file_id')
    query.append(r'and Stream.stream_index = Audio.stream_index')
    query.append(r'where')
    query.append(r'Stream.file_id = ?')
    query.append(r'order by')
    query.append(r'Stream.file_id, Stream.stream_index')
    param = (file_id,)
    
    result = []
    for audio_stream in sqlite3_utils.fetchall(conn, ' '.join(query), param):
        stream_entity = StreamEntity()
        stream_entity.file_id = audio_stream[0]
        stream_entity.stream_index = audio_stream[1]
        stream_entity.codec_type = audio_stream[2]
        stream_entity.codec_name = audio_stream[3]
        stream_entity.codec_long_name = audio_stream[4]
        stream_entity.duration = audio_stream[5]
        stream_entity.bit_rate = audio_stream[6]
        
        audio_entity = AudioEntity()
        audio_entity.file_id = audio_stream[0]
        audio_entity.stream_index = audio_stream[1]
        audio_entity.sample_rate = audio_stream[7]
        
        audio_stream_entity = AudioStreamEntity()
        audio_stream_entity.stream = stream_entity
        audio_stream_entity.audio = audio_entity
        
        result.append(audio_stream_entity)
    
    return result
