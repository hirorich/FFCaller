# ==================================================
# 動画変換ツール
# ==================================================

from service.converter import request_bean_parser
from service.converter import convert_command_creater
from service.common import command_runner

# 動画変換処理実行
def exec(request_json_string):
    
    print('converter')
    
    # リクエストjson文字列の解析
    request_bean = request_bean_parser.parse_to_request_bean(request_json_string)
    print(request_bean.get_output_file_bean().get_output_file_name())
    
    # コマンド作成
    command = convert_command_creater.create_command(request_bean)
    command = [r'ipconfig', r'/all']
    
    # 実行
    proc_stdout = command_runner.run(command)
    for line in proc_stdout:
        print(line)
    

