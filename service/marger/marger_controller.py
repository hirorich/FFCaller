# ==================================================
# 動画変換のコントロール部品
# ==================================================

from common.utility import command_utils, json_utils
from service.marger import marge_command_creater
from service.marger.bean.response_bean import MargerResponseBean

# 変換実行
def marge(request_bean):
    
    # コマンド作成
    command = marge_command_creater.create_command(request_bean)
    
    # 実行
    proc_stdout = command_utils.run(command, True)
    
    # 動画変換レスポンスBeanへセット
    response_bean = MargerResponseBean()
    response_bean.output_file_name = request_bean.output_file_bean.output_file_name
    return response_bean

