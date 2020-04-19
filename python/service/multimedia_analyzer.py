# ==================================================
# 動画解析ツール
# ==================================================

from service.analyzer import request_bean_parser
from service.analyzer import analyzer_controller
from service.common import json_utils
from service.common.bean.response_bean import ResponseBean

# 動画解析処理実行
def exec(request_json_string):
    
    print('analyzer')
    
    response_bean = ResponseBean()
    
    try:
        
        # リクエストjson文字列の解析
        request_bean = request_bean_parser.parse_to_request_bean(request_json_string)
        
        # 動画解析リクエストBeanへセット
        service_request_bean = request_bean.get_service_request_bean()
        
        # ffprobeを用いて動画情報取得
        service_response_bean = analyzer_controller.analize(service_request_bean)
        
        # レスポンスBeanへセット
        response_bean.set_service_response_bean(service_response_bean)
        
        # レスポンスBeanをレスポンスjson文字列に変換
        response_json_string = json_utils.encode(response_bean.parse_to_dict())
    
    except:
        response_bean.set_service_response_bean(None)
        response_json_string = json_utils.encode(response_bean.parse_to_dict())
    
    # レスポンスjson文字列を返却
    return response_json_string

