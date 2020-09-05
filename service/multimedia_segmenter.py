# ==================================================
# フレーム分割ツール
# ==================================================

import eel
from common.utility import log_utils
from service.segmenter import request_bean_parser
from service.segmenter import segmenter_controller

# javascriptからフレーム分割ツールを呼び出す
@eel.expose
def segment(request):
    
    try:
        segment_info = exec(request)
        eel.response_segment(segment_info)
    except Exception as e:
        message = log_utils.write_exception(e)
        eel.get_server_error_msg(message)

# フレーム分割処理実行
def exec(request_dict):
    
    print('segmenter')
    
    # リクエスト解析
    service_request_bean = request_bean_parser.parse_to_request_bean(request_dict)
    
    # ffmpegを用いてフレーム分割
    service_response_bean = segmenter_controller.segment(service_request_bean)
    
    # フレーム分割情報を辞書型に変換し返却
    return service_response_bean.parse_to_dict()

