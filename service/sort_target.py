# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import eel, sqlite3
from common import app_property
from common.utility import log_utils, path_utils
from service.ffc import ffc_update_target
from service.ffc.bean.input_target_bean import InputTargetBean

db_filename = path_utils.convert_to_absolute_path(app_property.add_data.ffc_db_sqlite3)

@eel.expose
def ffc_request_sort_target(request):
    
    # DB接続
    with sqlite3.connect(db_filename) as conn:
        try:
            input_target_bean_list = []
            for input_target_dict in request:
                bean = InputTargetBean()
                bean.target_id = input_target_dict['target_id']
                bean.item_order = input_target_dict['item_order']
                input_target_bean_list.append(bean)
            
            # 並び順を更新
            ffc_update_target.update_order(conn, input_target_bean_list)
            
            conn.commit()
        except Exception as e:
            conn.rollback()
            message = log_utils.write_exception(e)
