# ==================================================
# フレーム分割ツール
# ==================================================

from service.segmenter import request_bean_parser
from service.segmenter import segmenter_controller

# フレーム分割処理実行
def exec(request_dict):
    
    print('segmenter')
    
    # リクエスト解析
    service_request_bean = request_bean_parser.parse_to_request_bean(request_dict)
    
    # ffmpegを用いてフレーム分割
    service_response_bean = segmenter_controller.segment(service_request_bean)
    
    # フレーム分割情報を辞書型に変換し返却
    return service_response_bean.parse_to_dict()

