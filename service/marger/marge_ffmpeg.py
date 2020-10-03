# ==================================================
# マージ実行
# ==================================================

from common.error import error_id
from common.error.business_error import BusinessError
from common.utility import command_utils, file_utils
from service.marger import command_creater

# 実行
def marge(output_bean):
    
    # コマンド作成
    command = command_creater.create(output_bean)
    
    # 実行
    proc_stdout = command_utils.run(command, True)
    
    # 出力ファイルチェック
    if not file_utils.is_exists(output_bean.filepath):
        raise BusinessError(error_id.E0000002, output_bean.filepath)
