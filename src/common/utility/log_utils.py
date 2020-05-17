# ==================================================
# ログ共通部品
# ==================================================

import traceback
from common.error.business_error import BusinessError

# ログファイル出力
def write_log(message):
    
    path='./server.log'
    with open(path, mode='a', encoding='utf-8') as f:
        f.write(message)

# ログファイル出力
def writeline_log(message):
    write_log(message + '\n')

# 例外出力
def write_exception(e):
    
    # スタックトレースと例外メッセージ出力
    write_log(traceback.format_exc())
    
    # ビジネスエラーのメッセージを取得
    if isinstance(e, BusinessError):
        message = e.get_business_error_message()
    else:
        message = '不明なエラーが発生しました。詳細はログを確認してください。'
    
    # メッセージを出力し返却
    writeline_log(message)
    return message

