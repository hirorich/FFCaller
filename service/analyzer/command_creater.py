# ==================================================
# ffprobeを用いた動画解析コマンド生成
# ==================================================

from common import app_property
from common.error import error_id
from common.error.business_error import BusinessError
from common.utility import file_utils
from common.utility.type import str_utils

# コマンド生成
def create(filename):
    
    # === 入力チェック ===
    # 入力ファイル名が空白
    if str_utils.is_none_or_whitespace(filename):
        raise BusinessError(error_id.E0000001)
    
    # 入力ファイルが存在しない
    filename = filename.strip()
    if not file_utils.is_exists(filename):
        raise BusinessError(error_id.E0000002, filename)
    # ====================
    
    # コマンド生成
    command = [app_property.external_cmd.ffprobe, '-v', 'quiet', '-show_format', '-show_streams', '-print_format', 'json']
    command.append(filename)
    
    return command
