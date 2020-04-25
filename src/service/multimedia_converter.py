# ==================================================
# 動画変換ツール
# ==================================================

from service.converter import request_bean_parser
from service.converter import converter_controller
from service.common import json_utils
from service.common import log_utils
from service.common.bean.response_bean import ResponseBean

# 動画変換処理実行
def exec(request_json_string):
    
    print('converter')
    
    response_bean = ResponseBean()
    
    try:
        
        # リクエストjson文字列の解析
        request_bean = request_bean_parser.parse_to_request_bean(request_json_string)
        
        # 動画変換リクエストBeanへセット
        service_request_bean = request_bean.get_service_request_bean()
        
        # ffmpegを用いて動画変換
        service_response_bean = converter_controller.convert(service_request_bean)
        
        # レスポンスBeanへセット
        response_bean.set_service_response_bean(service_response_bean)
        
        # レスポンスBeanをレスポンスjson文字列に変換
        response_json_string = json_utils.encode(response_bean.parse_to_dict())
    
    except Exception as e:
        log_utils.write_log(e)
        response_bean.set_service_response_bean(None)
        response_json_string = json_utils.encode(response_bean.parse_to_dict())
    
    # レスポンスjson文字列を返却
    return response_json_string

