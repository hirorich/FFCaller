# ==================================================
# 動画解析ツール
# ==================================================

from service.analyzer import request_bean_parser
from service.analyzer import analyzer_controller
from service.analyzer.bean.analyzer_request_bean import AnalyzerRequestBean

# 動画解析処理実行
def exec(filename):
    
    print('analyzer')
    
    # 動画解析リクエストBeanへセット
    service_request_bean = AnalyzerRequestBean()
    service_request_bean.set_input_file_name(filename)
    
    # ffprobeを用いて動画情報取得
    service_response_bean = analyzer_controller.analize(service_request_bean)
    
    # レスポンスBeanへセット
    return service_response_bean.parse_to_dict()

