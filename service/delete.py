# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import eel, sqlite3
from common import app_property
from common.utility import log_utils, path_utils
from service.ffc import ffc_delete, ffc_response_target

db_filename = path_utils.convert_to_absolute_path(app_property.add_data.ffc_db_sqlite3)

@eel.expose
def ffc_request_delete_target(request):
    
    # DB接続
    with sqlite3.connect(db_filename) as conn:
        try:
            target_id = request['target_id']
            
            # ターゲット削除
            ffc_delete.delete_target(conn, target_id)
            
            # 動画情報を返却
            ffc_response_target.exec(conn)
            
            conn.commit()
        except Exception as e:
            conn.rollback()
            message = log_utils.write_exception(e)

def ffc_delete_all():
    
    # DB接続
    with sqlite3.connect(db_filename) as conn:
        try:
            
            # 全ファイル削除
            ffc_delete.delete_all(conn)
            
            conn.commit()
        except Exception as e:
            conn.rollback()
            message = log_utils.write_exception(e)
