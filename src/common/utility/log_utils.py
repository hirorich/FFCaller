# ==================================================
# ログ共通部品
# ==================================================

import traceback
from common.error import business_error
from common.error.business_error import BusinessError

# ログファイル出力
def write_log(message):
    
    # 例外の場合はスタックトレースも出力
    if isinstance(message, Exception):
        write_log(traceback.format_exc())
        if isinstance(message, BusinessError):
            __write_business_error(message)
        return
    
    path='./test.log'
    with open(path, mode='a', encoding='utf-8') as f:
        f.write(message)

# ビジネスエラーログ出力
def __write_business_error(business_error_object):
    
    if len(business_error_object.args) == 0:
        return
    
    # IDを基にメッセージ取得
    message_id = business_error_object.args[0]
    message = business_error.get_business_message(message_id)
    
    # ログ出力
    write_log(message)

