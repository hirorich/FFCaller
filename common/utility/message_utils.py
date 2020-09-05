# ==================================================
# メッセージ取得部品
# ==================================================

from common.utility import sqlite3_utils
from common.utility.type import str_utils

# メッセージ取得
def get_message(message_id, message_args):
    
    # メッセージIDのチェック
    if str_utils.is_none_or_whitespace(message_id):
        return 'メッセージID未指定'
    
    # idを基にメッセージ内容取得
    ret, message = select_tb_message(message_id)
    
    # メッセージが見つからない場合はメッセージが見つからない旨を返却
    if ret == False:
        return 'メッセージID未定義（ID:' + message_id + '）'
    
    # メッセージのパラメータを置換
    if message_args is not None:
        for i in range(len(message_args)):
            message = message.replace('%' + str(i), message_args[i])
    
    return message_id + '：' + message

# テーブルからメッセージ内容取得
def select_tb_message(message_id):
    
    # 実行するクエリを定義
    db_filename = './db/cmn_db.sqlite3'
    query = 'select id, message from tb_message where id = ?'
    param = (message_id,)
    
    # クエリ実行
    fetchone_result = sqlite3_utils.fetchone(db_filename, query, param)
    
    # 取得したメッセージを返却
    if fetchone_result is None:
        return False, None
    else:
        return True, fetchone_result[1]
