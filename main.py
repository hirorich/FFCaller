import eel
from common import app_property
from common.utility import log_utils
from service import choose_files, get_target_info

# main
if __name__ == "__main__":
    
    try:
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
