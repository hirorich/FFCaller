# ==================================================
# ターゲット一覧を返却
# ==================================================

import eel
from common.utility import log_utils
from service.ffc.sql import ffc_select

# 実行
def exec(conn):
    try:
        # ターゲット一覧取得
        response = []
        for input_target in ffc_select.get_input_target_list(conn):
            response.append(input_target.to_dict())
        
        eel.ffc_response_target_list(response)
        
    except Exception as e:
        message = log_utils.write_exception(e)
