# ==================================================
# ファイル共通部品
# ==================================================

import os
from tkinter import filedialog, Tk
from common.utility import log_utils
from common.utility.type import str_utils

# ファイルの存在チェック
def is_exists(parameter):
    
    # 入力ファイル名が空白
    if str_utils.is_none_or_whitespace(parameter):
        return False
    
    return os.path.exists(parameter)

# ファイルを1列の文字列として読み込む
def read_file_one_line(filename):
    stdout = ''
    with open(filename, encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            stdout += line.strip()
    
    return stdout

# ファイル削除
def delete_file(filename):
    try:
        os.remove(filename)
        return True
    except Exception as e:
        log_utils.write_exception(e)
        return False

# ファイル選択
def open_file_dialog(filetypes=None):
    if filetypes is None:
        filetypes = [('all files', '*.*')]
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    file_list = filedialog.askopenfilenames(filetypes=filetypes)
    root.destroy()
    
    return file_list
