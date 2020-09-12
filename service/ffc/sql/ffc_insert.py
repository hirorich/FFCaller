# ==================================================
# ffc_dbのデータ追加
# ==================================================

from common.utility import sqlite3_utils

# File追加
def insert_file(conn, file_entity):
    query = []
    query.append(r'inser into File')
    query.append(r'(file_id, filename, filepath, workpath, webpath)')
    query.append(r'VALUES')
    query.append(r'(?, ?, ?, ?, ?)')
    param = (file_entity.file_id, file_entity.filename, file_entity.filepath, file_entity.workpath, file_entity.webpath)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

