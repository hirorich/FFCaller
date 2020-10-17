# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import eel, sqlite3
from common import app_property
from common.utility import desktop_notify_utils, log_utils
from service.common.const import env_const
from service.ffc import ffc_marge
from service.marger import marge_ffmpeg

@eel.expose
def ffc_request_marge():
    
    try:
        
        # DB接続
        with sqlite3.connect(env_const.DB_FILENAME) as conn:
            
            # マージ情報取得
            output_bean = ffc_marge.exec(conn)
        
        # マージ実行
        marge_ffmpeg.marge(output_bean)
        
        desktop_notify_utils.notify(app_property.app_name, 'マージ完了')
    except Exception as e:
        message = log_utils.write_exception(e)
        desktop_notify_utils.notify(app_property.app_name, message)
