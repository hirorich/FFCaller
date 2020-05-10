import argparse
import pathlib

# eelのインポート
import eel

from common.utility import log_utils
from service import multimedia_analyzer, multimedia_marger, multimedia_segmenter

# エラーメッセージを返却する
def return_error_massage(e):
    try:
        eel.get_server_error_msg(e.args[0])
    except:
        eel.get_server_error_msg('不明なエラーが発生しました。詳細はログを確認してください。')

# javascriptから動画解析ツールを呼び出す
@eel.expose
def analyze(request):
    
    try:
        analyze_info = multimedia_analyzer.exec(request)
        eel.response_analyzer(analyze_info)
    except Exception as e:
        log_utils.write_log(e)
        return_error_massage(e)

# javascriptから動画変換ツールを呼び出す
@eel.expose
def marge_trim(request):
    
    try:
        convert_info = multimedia_marger.exec(request)
        eel.response_marge_trim(convert_info)
    except Exception as e:
        log_utils.write_log(e)
        return_error_massage(e)

# javascriptからフレーム分割ツールを呼び出す
@eel.expose
def segment(request):
    
    try:
        segment_info = multimedia_segmenter.exec(request)
        eel.response_segment(segment_info)
    except Exception as e:
        log_utils.write_log(e)
        return_error_massage(e)

# main
if __name__ == "__main__":
    
    try:
        # デフォルトの出力先フォルダ生成
        pathlib.Path('./_output/frame').mkdir(parents=True, exist_ok=True)
        
        # ウェブコンテンツを持つフォルダ
        eel.init('web')
        
        # 最初に表示するhtmlページ
        eel.start('index.html', mode='chrome', host='localhost', position=(400, 100), port=9090, size=(800, 600), cmdline_args=['--incognito'])
    except Exception as e:
        log_utils.write_log(e)
        log_utils.write_log('予期せぬエラーが発生しました')
