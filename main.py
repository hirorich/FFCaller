import eel, pathlib, shutil
from common import app_property
from common.utility import log_utils
from service import multimedia_analyzer, multimedia_marger, multimedia_segmenter

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
        eel.set_property(app_property.outdir)
    except Exception as e:
        message = log_utils.write_exception(e)
        eel.get_server_error_msg(message)

# 出力先フォルダ生成
def create_outdir():
    # 既存フォルダを削除
    shutil.rmtree(app_property.outdir, ignore_errors=True)
    
    # 新規フォルダ作成
    pathlib.Path(app_property.outdir + 'frame/').mkdir(parents=True, exist_ok=True)

# main
if __name__ == "__main__":
    
    try:
        # 出力先フォルダ生成
        create_outdir()
        
        # ウェブコンテンツを持つフォルダ
        eel.init(app_property.eel.init)
        
        # 最初に表示するhtmlページ
        eel.start(
            app_property.eel.start,
            mode = app_property.eel.mode,
            host = 'localhost',
            port = app_property.eel.port,
            position = app_property.eel.position,
            size = app_property.eel.size,
            cmdline_args = list(app_property.eel.cmdline_args)
        )
    except Exception as e:
        message = log_utils.write_exception(e)
        log_utils.writeline_fatal('予期せぬエラーが発生しました')
