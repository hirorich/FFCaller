# ==================================================
# json文字列から動画解析リクエストBeanの解析
# ==================================================

from service.common import json_utils
from service.common.bean.request_bean import RequestBean
from service.analyzer.bean.analyzer_request_bean import AnalyzerRequestBean

# リクエストjson文字列を解析してリクエストBeanを返却
def parse_to_request_bean(request_json_string):
    
    # json形式の文字列をdict型に変換
    bean_dict= json_utils.decode(request_json_string)
    
    # 動画解析リクエストBean に格納
    analyzer_request_bean = AnalyzerRequestBean()
    analyzer_request_bean.set_input_file_name(bean_dict['service_request']['input_file_name'])
    
    # リクエストBean に格納
    request_bean = RequestBean()
    request_bean.set_service_request_bean(analyzer_request_bean)
    
    # リクエストBean を返却
    return request_bean
    

