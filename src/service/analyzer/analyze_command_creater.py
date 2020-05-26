# ==================================================
# ffprobeを用いた動画解析コマンド生成
# ==================================================

from common.error import error_id
from common.error.business_error import BusinessError
from common.utility.type import str_utils
from common.utility import file_utils

# コマンド生成
def create_command(request_bean):
    
    # === 入力チェック ===
    # 入力ファイル名が空白
    input_file_name = request_bean.input_file_name
    if str_utils.is_none_or_whitespace(input_file_name):
        raise BusinessError(error_id.E0000001)
    
    # 入力ファイルが存在しない
    input_file_name = input_file_name.strip()
    if not file_utils.is_exists(input_file_name):
        raise BusinessError(error_id.E0000002, input_file_name)
    # ====================
    
    # コマンド生成
    command = [r'ffprobe', r'-v', r'quiet', r'-show_format', r'-show_streams', r'-print_format', r'json']
    command.append(input_file_name)
    
    return command

