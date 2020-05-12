# ==================================================
# メッセージ取得部品
# ==================================================

from common.utility.type import str_utils

# メッセージ取得
def get_message(message_id, message_args):
    
    # メッセージIDのチェック
    if str_utils.is_none_or_whitespace(message_id):
        return 'エラーメッセージID未指定'
    
    # idを基にメッセージ内容取得
    message, ret = select_tb_message(message_id)
    
    # メッセージが見つからない場合はメッセージが見つからない旨を返却
    if ret == False:
        return 'エラーメッセージID未定義（ID:' + message_id + '）'
    
    # メッセージのパラメータを置換
    if message_args is not None:
        for i in range(len(message_args)):
            message = message.replace('%' + str(i), message_args[i])
    
    return message

# テーブルからメッセージ内容取得
def select_tb_message(message_id):
    return '%0-さんぷる_%1.メッセージ"%2"%2', True
