# ==================================================
# ビジネスエラー部品
# ==================================================

from common.utility.type import str_utils

# ビジネスエラークラス
class BusinessError(Exception):
    pass

# IDを基にメッセージ取得
def get_business_message(message_id):
    
    try:
        
        if str_utils.is_none_or_whitespace(message_id):
            return 'メッセージIDが指定されていません'
        
        # IDを基にメッセージ取得
        
        # メッセージが見つからない場合はメッセージが見つからない旨を返却
        return 'メッセージは定義されていません（メッセージID:' + message_id + '）'
        
    except:
        # 例外が発生した場合はメッセージ取得に失敗した旨を返却
        return 'メッセージの取得に失敗しました（メッセージID:' + message_id + '）'

