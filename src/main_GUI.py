# eelのインポート
import eel

from service.common import log_utils
from service import multimedia_analyzer

#javascriptからpythonを呼び出す
@eel.expose
def analyze(filename):
    
    try:
        analyze_info = multimedia_analyzer.exec_local(filename)
        eel.response_analyzer(analyze_info)
    except Exception as e:
        log_utils.write_log(e)
        eel.get_server_error_msg('ローカルサーバでエラーが発生しました')

# main
if __name__ == "__main__":
    
    # ウエブコンテンツを持つフォルダー
    eel.init('web')
    
    # 最初に表示するhtmlページ
    eel.start('index.html', mode='chrome', host='localhost', position=(400, 100), port=9090, size=(800, 600))
