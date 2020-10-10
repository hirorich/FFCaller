# ==================================================
# ffprobeを用いた動画解析
# ==================================================

import json
from common.utility import command_utils
from service.analyzer import command_creater

# 解析実行
def analize(filename):
    
    # コマンド作成
    command = command_creater.create(filename)
    
    # 実行
    proc_stdout = command_utils.run(command, True)
    
    # json文字列から辞書型に変換
    return json.loads(''.join(proc_stdout))
