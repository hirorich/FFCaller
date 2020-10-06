# ==================================================
# ffc_dbのデータ削除
# ==================================================

from common.utility import sqlite3_utils

# Target削除
def delete_target(conn, target_id):
    query = []
    query.append(r'delete from Target')
    query.append(r'where')
    query.append(r'target_id = ?')
    param = (target_id,)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Target全削除
def delete_target_all(conn):
    query = []
    query.append(r'delete from Target')
    
    sqlite3_utils.execute(conn, ' '.join(query))

# Trim削除
def delete_trim(conn, target_id):
    query = []
    query.append(r'delete from Trim')
    query.append(r'where')
    query.append(r'target_id = ?')
    param = (target_id,)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Trim全削除
def delete_trim_all(conn):
    query = []
    query.append(r'delete from Trim')
    
    sqlite3_utils.execute(conn, ' '.join(query))

# File削除
def delete_file(conn, file_id):
    query = []
    query.append(r'delete from File')
    query.append(r'where')
    query.append(r'file_id = ?')
    param = (file_id,)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# File全削除
def delete_file_all(conn):
    query = []
    query.append(r'delete from File')
    
    sqlite3_utils.execute(conn, ' '.join(query))

# Format削除
def delete_format(conn, file_id):
    query = []
    query.append(r'delete from Format')
    query.append(r'where')
    query.append(r'file_id = ?')
    param = (file_id,)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Format全削除
def delete_format_all(conn):
    query = []
    query.append(r'delete from Format')
    
    sqlite3_utils.execute(conn, ' '.join(query))

# Stream削除
def delete_stream(conn, file_id):
    query = []
    query.append(r'delete from Stream')
    query.append(r'where')
    query.append(r'file_id = ?')
    param = (file_id,)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Stream全削除
def delete_stream_all(conn):
    query = []
    query.append(r'delete from Stream')
    
    sqlite3_utils.execute(conn, ' '.join(query))

# Video削除
def delete_video(conn, file_id):
    query = []
    query.append(r'delete from Video')
    query.append(r'where')
    query.append(r'file_id = ?')
    param = (file_id,)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Video全削除
def delete_video_all(conn):
    query = []
    query.append(r'delete from Video')
    
    sqlite3_utils.execute(conn, ' '.join(query))

# Audio削除
def delete_audio(conn, file_id):
    query = []
    query.append(r'delete from Audio')
    query.append(r'where')
    query.append(r'file_id = ?')
    param = (file_id,)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Audio全削除
def delete_audio_all(conn):
    query = []
    query.append(r'delete from Audio')
    
    sqlite3_utils.execute(conn, ' '.join(query))
