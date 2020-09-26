# ==================================================
# 動画情報を返却
# ==================================================

import eel
from common.utility import log_utils
from service.ffc.sql import ffc_add_files_sql, ffc_select

# 実行
def exec(conn, target_id):
    try:
        # 動画情報取得
        target = ffc_select.get_target(conn, target_id)
        file_id = target.file_id
        trim = ffc_select.get_trim(conn, target_id)
        file = ffc_select.get_file(conn, file_id)
        video_stream = ffc_select.get_video_stream(conn, file_id)
        audio_streams = ffc_select.get_audio_streams(conn, file_id)
        file_duration_entity = ffc_add_files_sql.get_file_duration(conn, file_id)
        
        # 動画情報設定
        response = dict()
        response['target_id'] = target_id
        response['trim'] = trim.to_dict()
        response['webpath'] = file.webpath
        response['duration'] = file_duration_entity.duration
        response['nb_frames'] = file_duration_entity.nb_frames
        response['with_video'] = (video_stream is not None)
        response['with_audio'] = (len(audio_streams) > 0)
        if response['with_video']:
            r_frame_rate = video_stream.video.r_frame_rate.split('/')
            response['r_frame_rate_numer'] = int(r_frame_rate[0])
            response['r_frame_rate_denom'] = int(r_frame_rate[1])
        elif response['with_audio']:
            response['r_frame_rate_numer'] = 0
            response['r_frame_rate_denom'] = 1
        
        eel.ffc_response_trim_info(response)
        
    except Exception as e:
        message = log_utils.write_exception(e)
