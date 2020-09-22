# ==================================================
# ffc_dbの情報取得
# ==================================================

from common.utility import sqlite3_utils
from service.ffc.entity.work_file_duration_entity import FileDurationEntity

# ファイルの長さ取得クエリ作成
def __create_query_get_file_duration():
    query = []
    query.append(r'select')
    query.append(r'File.file_id as file_id, Format.duration as duration, Video.nb_frames as nb_frames')
    query.append(r'from File')
    query.append(r'inner join Format')
    query.append(r'on File.file_id = Format.file_id')
    query.append(r'inner join Stream')
    query.append(r'on File.file_id = Stream.file_id')
    query.append(r'left outer join Video')
    query.append(r'on Stream.file_id = Video.file_id and Stream.stream_index = Video.stream_index')
    
    return query

# ファイルIDよりファイルの長さ取得
def get_file_duration_by_id(conn, file_id):
    query = __create_query_get_file_duration()
    query.append(r'where')
    query.append(r'File.file_id = ?')
    param = (file_id,)
    
    result = sqlite3_utils.fetchall(conn, ' '.join(query), param)
    entity = FileDurationEntity()
    if len(result) != 0:
        entity.file_id = result[0][0]
        entity.trim_duration = result[0][1]
        if result[0][2] is not None:
            entity.nb_frames = result[0][2]
    
    return entity

# ファイルパスよりファイルの長さ取得
def get_file_duration_by_path(conn, filepath):
    query = __create_query_get_file_duration()
    query.append(r'where')
    query.append(r'File.filepath = ?')
    param = (filepath,)
    
    result = sqlite3_utils.fetchall(conn, ' '.join(query), param)
    entity = FileDurationEntity()
    if len(result) != 0:
        entity.file_id = result[0][0]
        entity.trim_duration = result[0][1]
        if result[0][2] is not None:
            entity.nb_frames = result[0][2]
    
    return entity

# ファイルIDの最大値取得
def get_max_file_id(conn):
    query = []
    query.append(r'select')
    query.append(r'max(file_id) as max_file_id')
    query.append(r'from File')
    
    result = sqlite3_utils.fetchall(conn, ' '.join(query))
    if len(result) == 0:
        return 0
    elif result[0][0] is None:
        return 0
    else:
        return result[0][0]

# ターゲットIDの最大値取得
def get_max_target_id(conn):
    query = []
    query.append(r'select')
    query.append(r'max(target_id) as max_target_id')
    query.append(r'from Target')
    
    result = sqlite3_utils.fetchall(conn, ' '.join(query))
    if len(result) == 0:
        return 0
    elif result[0][0] is None:
        return 0
    else:
        return result[0][0]

# 並び順の最大値取得
def get_max_item_order(conn):
    query = []
    query.append(r'select')
    query.append(r'max(item_order) as max_item_order')
    query.append(r'from Target')
    
    result = sqlite3_utils.fetchall(conn, ' '.join(query))
    if len(result) == 0:
        return 0
    elif result[0][0] is None:
        return 0
    else:
        return result[0][0]
