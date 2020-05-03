# ==================================================
# 動画変換のコントロール部品
# ==================================================

from service.marger import marge_command_creater
from service.marger.bean.response_bean import ResponseBean
from service.common import command_runner, json_utils

# 変換実行
def marge(request_bean):
    
    # コマンド作成
    command = marge_command_creater.create_command(request_bean)
    
    # 実行
    proc_stdout = command_runner.run(command, True)
    
    # 動画変換レスポンスBeanへセット
    response_bean = ResponseBean()
    response_bean.set_output_file_name(request_bean.get_output_file_bean().get_output_file_name())
    return response_bean

