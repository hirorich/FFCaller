# ==================================================
# json文字列から動画解析リクエストBeanの解析
# ==================================================

from service.common import json_utils
from service.analyzer.bean.request_bean import AnalyzerRequestBean

# リクエストjson文字列を解析してリクエストBeanを返却
def parse_to_request_bean(request_dict):
    
    # 動画解析リクエストBean に格納
    analyzer_request_bean = AnalyzerRequestBean()
    analyzer_request_bean.set_input_file_name(request_dict['input_file_name'])
    
    # 動画解析リクエストBean を返却
    return analyzer_request_bean

