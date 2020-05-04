# ==================================================
# ffprobeを用いた動画解析コマンド生成
# ==================================================

from common.utility.type import str_utils
from common.utility import file_utils

# コマンド生成
def create_command(request_bean):
    
    # === 入力チェック ===
    # 入力ファイル名が空白
    input = request_bean.input_file_name
    if str_utils.is_none_or_whitespace(input):
        raise Exception('input_file is not specified')
    
    # 入力ファイルが存在しない
    input = input.strip()
    if not file_utils.is_exists(input):
        raise Exception(input + ' is not exists')
    # ====================
    
    # コマンド生成
    command = [r'ffprobe', r'-v', r'quiet', r'-show_format', r'-show_streams', r'-print_format', r'json']
    command.append(input)
    
    return command

