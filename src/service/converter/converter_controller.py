# ==================================================
# 動画変換のコントロール部品
# ==================================================

from service.converter import convert_command_creater
from service.converter.bean.converter_response_bean import ConverterResponseBean
from service.common import command_runner
from service.common import json_utils

# 変換実行
def convert(request_bean):
    
    # コマンド作成
    command = convert_command_creater.create_command(request_bean)
    
    # 実行
    proc_stdout = command_runner.run(command, True)
    
    # 動画変換レスポンスBeanへセット
    response_bean = ConverterResponseBean()
    response_bean.set_output_file_name('output.mp4')
    return response_bean
    

