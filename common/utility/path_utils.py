# ==================================================
# パス操作部品
# ==================================================

import os, sys, pathlib

# 相対パスから絶対パス
def convert_to_absolute_path(relative_path):
    
    # 基点
    try:
        # pyinstaller用
        base_path = pathlib.Path(sys._MEIPASS)
    except:
        base_path = pathlib.Path(os.getcwd())
    
    # 絶対パスに変換
    return str(base_path.joinpath(relative_path))
