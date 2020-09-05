# ==================================================
# 動画解析ツール
# ==================================================

import eel
from common.utility import log_utils
from service.analyzer import request_bean_parser
from service.analyzer import analyzer_controller

# javascriptから動画解析ツールを呼び出す
@eel.expose
def analyze(request):
    
    try:
        analyze_info = exec(request)
        eel.response_analyzer(analyze_info)
    except Exception as e:
        message = log_utils.write_exception(e)
        eel.common_response_error_msg(message)

# 動画解析処理実行
def exec(request_dict):
    
    print('analyzer')
    
    # 動画解析リクエストBeanへセット
    service_request_bean= request_bean_parser.parse_to_request_bean(request_dict)
    
    # ffprobeを用いて動画情報取得
    service_response_bean = analyzer_controller.analize(service_request_bean)
    
    # 動画情報を辞書型に変換し返却
    return service_response_bean.parse_to_dict()

