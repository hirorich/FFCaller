# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import eel, sqlite3
from common import app_property
from common.utility import log_utils, path_utils
from service.ffc import ffc_add_files, ffc_response_target

@eel.expose
def ffc_request_choose_files():
    
    try:
        
        # DB接続
        db_filename = path_utils.convert_to_absolute_path(app_property.add_data.ffc_db_sqlite3)
        with sqlite3.connect(db_filename) as conn:
            
            # 対象ファイル追加
            ffc_add_files.exec(conn)
            
            # 追加後情報を返却
            ffc_response_target.exec(conn)
            
            # 追加情報反映
            conn.commit()
        
    except Exception as e:
        message = log_utils.write_exception(e)
