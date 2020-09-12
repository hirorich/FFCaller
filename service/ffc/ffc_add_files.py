# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import pathlib, shutil
from common import app_property
from common.utility import file_utils, log_utils, path_utils
from service.analyzer import analyzer_ffprobe
from service.ffc.sql import ffc_insert, ffc_searcher
from service.ffc.entity.file_entity import FileEntity

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
            
            # 対象ID発行
            # トリム情報DB登録
            
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
    file_duration_entity = ffc_searcher.get_file_duration_by_path(conn, file_entity.filepath)
    if file_duration_entity.file_id is not None:
        return file_duration_entity
    
    # ファイルID発行
    file_entity.file_id = ffc_searcher.get_max_file_id(conn) + 1
    
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
    
    # ファイルテーブル追加
    ffc_insert.insert_file(conn, file_entity)
    
    # 登録情報返却
    return ffc_searcher.get_file_duration_by_id(conn, file_entity.file_id)
