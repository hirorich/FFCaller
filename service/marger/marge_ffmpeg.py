# ==================================================
# マージ実行
# ==================================================

from common.utility import command_utils
from service.marger import command_creater

# 実行
def marge(output_bean):
    
    # コマンド作成
    command_creater.create(output_bean)
    
    # 実行
    proc_stdout = command_utils.run(command, True)
