# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import eel, sqlite3
from common import app_property
from common.utility import log_utils, path_utils
from service.ffc import ffc_response_media_info, ffc_response_trim_info

db_filename = path_utils.convert_to_absolute_path(app_property.add_data.ffc_db_sqlite3)

@eel.expose
def ffc_request_get_media_info(request):
    
    # DB接続
    with sqlite3.connect(db_filename) as conn:
        try:
            target_id = request['target_id']
            
            # 動画情報を返却
            ffc_response_media_info.exec(conn, target_id)
            
        except Exception as e:
            message = log_utils.write_exception(e)

@eel.expose
def ffc_request_get_trim_info(request):
    
    # DB接続
    with sqlite3.connect(db_filename) as conn:
        try:
            target_id = request['target_id']
            
            # 動画情報を返却
            ffc_response_trim_info.exec(conn, target_id)
            
        except Exception as e:
            message = log_utils.write_exception(e)
