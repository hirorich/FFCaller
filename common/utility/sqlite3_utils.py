# ==================================================
# sqlite3共通部品
# ==================================================

import sqlite3

# 1行取得
def fetchone(db_filename, query, param):
    
    result = None
    
    with sqlite3.connect(db_filename) as conn:
        
        cursor = conn.cursor()
        
        # クエリ実行
        cursor.execute(query, param)
        
        result = cursor.fetchone()
    
    # 取得結果を返却
    # 対象行が0行だった場合はNoneが返却される
    return result

# 複数行取得
def fetchall(conn, query, param=None):
    cursor = conn.cursor()
    
    # クエリ実行
    if param is None:
        cursor.execute(query)
    else:
        cursor.execute(query, param)
    
    return cursor.fetchall()

# クエリ実行
def execute(conn, query, param=None):
    cursor = conn.cursor()
    
    # クエリ実行
    if param is None:
        cursor.execute(query)
    else:
        cursor.execute(query, param)
