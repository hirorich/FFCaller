# ==================================================
# ffc_dbの情報取得
# ==================================================

from common.utility import sqlite3_utils
from service.ffc.entity.work_file_duration_entity import FileDurationEntity

# ファイルの長さ取得クエリ作成
def __create_query_get_video_duration():
    query = []
    query.append(r'select')
    query.append(r'File.file_id as file_id, Stream.duration as duration, Video.nb_frames as nb_frames')
    query.append(r'from File')
    query.append(r'inner join Stream')
    query.append(r'on File.file_id = Stream.file_id')
    query.append(r'inner join Video')
    query.append(r'on Stream.file_id = Video.file_id and Stream.stream_index = Video.stream_index')
    
    return query

# ファイルの長さ取得クエリ作成
def __create_query_get_audio_duration():
    query = []
    query.append(r'select')
    query.append(r'File.file_id as file_id, Stream.duration as duration')
    query.append(r'from File')
    query.append(r'inner join Stream')
    query.append(r'on File.file_id = Stream.file_id')
    query.append(r'inner join Audio')
    query.append(r'on Stream.file_id = Audio.file_id and Stream.stream_index = Audio.stream_index')
    
    return query

# ファイルIDよりファイルの長さ取得
def get_file_duration_by_id(conn, file_id):
    query = __create_query_get_video_duration()
    query.append(r'where')
    query.append(r'File.file_id = ?')
    param = (file_id,)
    result_video = sqlite3_utils.fetchall(conn, ' '.join(query), param)
    
    query = __create_query_get_audio_duration()
    query.append(r'where')
    query.append(r'File.file_id = ?')
    param = (file_id,)
    result_audio = sqlite3_utils.fetchall(conn, ' '.join(query), param)
    
    entity = FileDurationEntity()
    if len(result_video) != 0:
        entity.file_id = result_video[0][0]
        entity.duration = result_video[0][1]
        entity.nb_frames = result_video[0][2]
    elif len(result_audio) != 0:
        entity.file_id = result_audio[0][0]
        entity.duration = result_audio[0][1]
    
    return entity

# ファイルパスよりファイルの長さ取得
def get_file_duration_by_path(conn, filepath):
    query = __create_query_get_video_duration()
    query.append(r'where')
    query.append(r'File.filepath = ?')
    param = (filepath,)
    result_video = sqlite3_utils.fetchall(conn, ' '.join(query), param)
    
    query = __create_query_get_audio_duration()
    query.append(r'where')
    query.append(r'File.filepath = ?')
    param = (filepath,)
    result_audio = sqlite3_utils.fetchall(conn, ' '.join(query), param)
    
    entity = FileDurationEntity()
    if len(result_video) != 0:
        entity.file_id = result_video[0][0]
        entity.duration = result_video[0][1]
        entity.nb_frames = result_video[0][2]
    elif len(result_audio) != 0:
        entity.file_id = result_audio[0][0]
        entity.duration = result_audio[0][1]
    
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
