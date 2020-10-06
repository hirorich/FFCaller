# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import eel, sqlite3
from common import app_property
from common.utility import log_utils, path_utils
from service.ffc import ffc_delete, ffc_response_target

@eel.expose
def ffc_request_delete_target(request):
    
    try:
        
        target_id = request['target_id']
        
        # DB接続
        db_filename = path_utils.convert_to_absolute_path(app_property.add_data.ffc_db_sqlite3)
        with sqlite3.connect(db_filename) as conn:
            
            # ターゲット削除
            ffc_delete.delete_target(conn, target_id)
            
            # 動画情報を返却
            ffc_response_target.exec(conn)
        
    except Exception as e:
        message = log_utils.write_exception(e)

def ffc_delete_all():
    
    try:
        
        # DB接続
        db_filename = path_utils.convert_to_absolute_path(app_property.add_data.ffc_db_sqlite3)
        with sqlite3.connect(db_filename) as conn:
            
            # 全ファイル削除
            ffc_delete.delete_all(conn)
        
    except Exception as e:
        message = log_utils.write_exception(e)
