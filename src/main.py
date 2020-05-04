# 起動引数使用のため
import argparse

# eelのインポート
import eel

from common.utility import log_utils
from service import multimedia_analyzer, multimedia_marger, multimedia_segmenter

# javascriptから動画解析ツールを呼び出す
@eel.expose
def analyze(request):
    
    try:
        analyze_info = multimedia_analyzer.exec(request)
        eel.response_analyzer(analyze_info)
    except Exception as e:
        log_utils.write_log(e)
        eel.get_server_error_msg('ローカルサーバでエラーが発生しました')

# javascriptから動画変換ツールを呼び出す
@eel.expose
def marge_trim(request):
    
    try:
        convert_info = multimedia_marger.exec(request)
        eel.response_marge_trim(convert_info)
    except Exception as e:
        log_utils.write_log(e)
        eel.get_server_error_msg('ローカルサーバでエラーが発生しました')

# javascriptからフレーム分割ツールを呼び出す
@eel.expose
def segment(request):
    
    try:
        segment_info = multimedia_segmenter.exec(request)
        eel.response_segment(segment_info)
    except Exception as e:
        log_utils.write_log(e)
        eel.get_server_error_msg('ローカルサーバでエラーが発生しました')

# main
if __name__ == "__main__":
    
    # ウェブコンテンツを持つフォルダー
    eel.init('web')
    
    # 最初に表示するhtmlページ
    eel.start('index.html', mode='chrome', host='localhost', position=(400, 100), port=9090, size=(800, 600), cmdline_args=['--incognito'])
