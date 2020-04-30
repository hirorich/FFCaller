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
    

# 
def read_file_one_line(filename):
    stdout = ''
    with open(filename, encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            stdout += line.strip()
    
    return stdout
