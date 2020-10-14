# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

import eel, sqlite3
from common import app_property
from common.utility import log_utils, path_utils
from service.ffc import ffc_response_target, ffc_update_trim
from service.ffc.entity.trim_entity import TrimEntity

db_filename = path_utils.convert_to_absolute_path(app_property.add_data.ffc_db_sqlite3)

@eel.expose
def ffc_request_update_trim_info(request):
    
    # DB接続
    with sqlite3.connect(db_filename) as conn:
        try:
            
            trim_entity = TrimEntity()
            trim_entity.target_id = request['target_id']
            trim_entity.start_time = request['trim']['start_time']
            trim_entity.end_time = request['trim']['end_time']
            trim_entity.start_frame = request['trim']['start_frame']
            trim_entity.end_frame = request['trim']['end_frame']
            trim_entity.frame_input_flag = request['trim']['frame_input_flag']
            trim_entity.video_fade_in = request['trim']['video_fade_in']
            trim_entity.video_fade_out = request['trim']['video_fade_out']
            trim_entity.audio_fade_in = request['trim']['audio_fade_in']
            trim_entity.audio_fade_out = request['trim']['audio_fade_out']
            
            # トリム情報更新
            ffc_update_trim.exec(conn, trim_entity)
            
            # 動画情報を返却
            ffc_response_target.exec(conn)
            
            conn.commit()
        except Exception as e:
            conn.rollback()
            message = log_utils.write_exception(e)
