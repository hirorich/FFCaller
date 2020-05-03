# ==================================================
# 動画変換ツール
# ==================================================

from service.converter import request_bean_parser
from service.converter import converter_controller

# 動画変換処理実行
def exec(request_dict):
    
    print('converter')
    
    # リクエスト解析
    service_request_bean = request_bean_parser.parse_to_request_bean(request_dict)
    
    # ffmpegを用いて動画変換
    service_response_bean = converter_controller.convert(service_request_bean)
    
    # レスポンスBeanをレスポンスjson文字列に変換
    response_json_string = service_response_bean.parse_to_dict()
    
    # レスポンスjson文字列を返却
    return response_json_string

