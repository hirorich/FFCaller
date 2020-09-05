# ==================================================
# 動画変換ツール
# ==================================================

import eel
from common.utility import log_utils
from service.marger import request_bean_parser
from service.marger import marger_controller

# javascriptから動画変換ツールを呼び出す
@eel.expose
def marge_trim(request):
    
    try:
        convert_info = exec(request)
        eel.response_marge_trim(convert_info)
    except Exception as e:
        message = log_utils.write_exception(e)
        eel.common_response_error_msg(message)

# 動画変換処理実行
def exec(request_dict):
    
    print('marger')
    
    # リクエスト解析
    service_request_bean = request_bean_parser.parse_to_request_bean(request_dict)
    
    # ffmpegを用いて動画変換
    service_response_bean = marger_controller.marge(service_request_bean)
    
    # 動画変換情報を辞書型に変換し返却
    return service_response_bean.parse_to_dict()

