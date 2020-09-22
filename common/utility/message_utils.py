# ==================================================
# メッセージ取得部品
# ==================================================

import sqlite3
from common import app_property
from common.utility import path_utils, sqlite3_utils
from common.utility.type import str_utils

# IDを基にメッセージ取得
def get_business_error_message(business_error):
    
    try:
        
        # メッセージ指定チェック
        if len(business_error.args) == 0:
            return 'エラーメッセージ未指定'
        
        # メッセージIDとパラメータ取得
        message_id = business_error.args[0]
        if len(business_error.args) >= 2:
            message_args = business_error.args[1:]
        else:
            message_args = None
        
        # メッセージ取得
        return get_message(message_id, message_args)
        
    except:
        # 例外が発生した場合はメッセージ取得に失敗した旨を返却
        return 'エラーメッセージの取得失敗'

# メッセージ取得
def get_message(message_id, message_args = None):
    
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
    
    return message_id + '：\n' + message.replace('\\n', '\n')

# テーブルからメッセージ内容取得
def select_tb_message(message_id):
    
    # 実行するクエリを定義
    db_filename = path_utils.convert_to_absolute_path(app_property.add_data.cmn_db_sqlite3)
    query = 'select id, message from tb_message where id = ?'
    param = (message_id,)
    
    # クエリ実行
    result = None
    with sqlite3.connect(db_filename) as conn:
        result = sqlite3_utils.fetchone(conn, query, param)
    
    # 取得したメッセージを返却
    if result is None:
        return False, None
    else:
        return True, result[1]
