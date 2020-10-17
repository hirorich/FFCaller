# ==================================================
# 動画情報を返却
# ==================================================

import eel
from common.utility import log_utils
from service.ffc.sql import ffc_select

# 実行
def exec(conn, target_id):
    try:
        # 動画情報取得
        target = ffc_select.get_target(conn, target_id)
        file_id = target.file_id
        file = ffc_select.get_file(conn, file_id)
        format = ffc_select.get_format(conn, file_id)
        video_stream = ffc_select.get_video_stream(conn, file_id)
        audio_streams = ffc_select.get_audio_streams(conn, file_id)
        
        # 動画情報設定
        response = dict()
        response['file'] = dict()
        response['file']['filepath'] = file.filepath
        response['format'] = format.to_dict()
        if video_stream is not None:
            response['video_stream'] = video_stream.to_dict()
        if len(audio_streams) > 0:
            response['audio_stream'] = audio_streams[0].to_dict()
        
        eel.ffc_response_media_info(response)
        
    except Exception as e:
        message = log_utils.write_exception(e)
