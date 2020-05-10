# ==================================================
# ログ共通部品
# ==================================================

import traceback
from common.error.business_error import BusinessError

# ログファイル出力
def write_log(message):
    
    # 例外の場合はスタックトレースも出力
    if isinstance(message, Exception):
        if isinstance(message, BusinessError):
            __write_business_error(message)
        else:
            write_log(traceback.format_exc())
        return
    
    path='./server.log'
    with open(path, mode='a', encoding='utf-8') as f:
        f.write(message)

# ビジネスエラーログ出力
def __write_business_error(business_error):
    
    # ビジネスエラーメッセージ取得
    business_error.set_business_error_message()
    
    # ログ出力
    write_log(traceback.format_exc())

