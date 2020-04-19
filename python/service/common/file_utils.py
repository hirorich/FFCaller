# ==================================================
# ファイル共通部品
# ==================================================

import os
from service.common.type import str_utils

# 
def is_exists(parameter):
    
    # 入力ファイル名が空白
    if str_utils.is_none_or_whitespace(parameter):
        return False
    
    return os.path.exists(parameter)
    

