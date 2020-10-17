# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import eel, sqlite3
from common.utility import log_utils
from service.common.const import env_const
from service.ffc import ffc_add_files, ffc_response_target

@eel.expose
def ffc_request_choose_files():
    
    # DB接続
    with sqlite3.connect(env_const.DB_FILENAME) as conn:
        try:
            
            # 対象ファイル追加
            ffc_add_files.exec(conn)
            
            # 追加後情報を返却
            ffc_response_target.exec(conn)
            
            # 追加情報反映
            conn.commit()
        except Exception as e:
            conn.rollback()
            message = log_utils.write_exception(e)
