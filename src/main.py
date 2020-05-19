import argparse
import pathlib, shutil

# eelのインポート
import eel

from common.utility import log_utils
from service import multimedia_analyzer, multimedia_marger, multimedia_segmenter
from service.common import property

# javascriptから動画解析ツールを呼び出す
@eel.expose
def analyze(request):
    
    try:
        analyze_info = multimedia_analyzer.exec(request)
        eel.response_analyzer(analyze_info)
    except Exception as e:
        message = log_utils.write_exception(e)
        eel.get_server_error_msg(message)

# javascriptから動画変換ツールを呼び出す
@eel.expose
def marge_trim(request):
    
    try:
        convert_info = multimedia_marger.exec(request)
        eel.response_marge_trim(convert_info)
    except Exception as e:
        message = log_utils.write_exception(e)
        eel.get_server_error_msg(message)

# javascriptからフレーム分割ツールを呼び出す
@eel.expose
def segment(request):
    
    try:
        segment_info = multimedia_segmenter.exec(request)
        eel.response_segment(segment_info)
    except Exception as e:
        message = log_utils.write_exception(e)
        eel.get_server_error_msg(message)

# javascriptから出力先フォルダクリアを呼び出す
@eel.expose
def clear_outdir():
    
    try:
        create_outdir()
    except Exception as e:
        message = log_utils.write_exception(e)
        eel.get_server_error_msg(message)

# javascriptからプロパティ情報を取得する
@eel.expose
def get_property():
    
    try:
        eel.set_property(property.outdir)
    except Exception as e:
        message = log_utils.write_exception(e)
        eel.get_server_error_msg(message)

# 出力先フォルダ生成
def create_outdir():
    # 既存フォルダを削除
    shutil.rmtree(property.outdir, ignore_errors=True)
    
    # 新規フォルダ作成
    pathlib.Path(property.outdir + 'frame/').mkdir(parents=True, exist_ok=True)

# main
if __name__ == "__main__":
    
    try:
        # 設定ファイル読み込み
        property.property_file = './env/property.json'
        property.read_property_file()
        
        # 出力先フォルダ生成
        create_outdir()
        
        # ウェブコンテンツを持つフォルダ
        eel.init('web')
        
        # 最初に表示するhtmlページ
        eel.start('index.html', mode=property.browser, host='localhost', position=(400, 100), port=property.port, size=(800, 600), cmdline_args=['--incognito'])
    except Exception as e:
        message = log_utils.write_exception(e)
        log_utils.write_log('予期せぬエラーが発生しました')
