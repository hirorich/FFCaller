# ==================================================
# 動画解析ツール
# ==================================================

from service.analyzer import request_bean_parser
from service.analyzer import analyzer_controller

# 動画解析処理実行
def exec(request_dict):
    
    print('analyzer')
    
    # 動画解析リクエストBeanへセット
    service_request_bean= request_bean_parser.parse_to_request_bean(request_dict)
    
    # ffprobeを用いて動画情報取得
    service_response_bean = analyzer_controller.analize(service_request_bean)
    
    # 動画情報を辞書型に変換し返却
    return service_response_bean.parse_to_dict()

