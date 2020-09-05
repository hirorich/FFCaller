# ==================================================
# 動画変換ツール
# ==================================================

from service.marger import request_bean_parser
from service.marger import marger_controller

# 動画変換処理実行
def exec(request_dict):
    
    print('marger')
    
    # リクエスト解析
    service_request_bean = request_bean_parser.parse_to_request_bean(request_dict)
    
    # ffmpegを用いて動画変換
    service_response_bean = marger_controller.marge(service_request_bean)
    
    # 動画変換情報を辞書型に変換し返却
    return service_response_bean.parse_to_dict()

