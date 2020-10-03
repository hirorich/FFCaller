# ==================================================
# ターゲット一覧を返却
# ==================================================

import eel
from common.utility import log_utils
from service.ffc.entity.work_input_target_entity import InputTargetEntity
from service.ffc.sql import ffc_select

# 実行
def exec(conn):
    try:
        # ターゲット一覧取得
        response = []
        for target in ffc_select.get_targets(conn):
            
            trim = ffc_select.get_trim(conn, target.target_id)
            file = ffc_select.get_file(conn, target.file_id)
            
            input_target = InputTargetEntity()
            input_target.target_id = target.target_id
            input_target.filename = file.filename
            input_target.filepath = file.filepath
            input_target.start_time = trim.start_time
            input_target.end_time = trim.end_time
            input_target.item_order = target.item_order
            response.append(input_target.to_dict())
        
        eel.ffc_response_target_list(response)
        
    except Exception as e:
        message = log_utils.write_exception(e)
