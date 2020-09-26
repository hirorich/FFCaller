# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

from common import app_property
from common.utility import log_utils
from service.ffc import ffc_convert
from service.ffc.sql import ffc_add_files_sql, ffc_select, ffc_update

# 実行
def exec(conn, trim_entity):
    try:
        
        # 入力値チェック
        if (not _check(conn, trim_entity)):
            return
        
        # DB更新
        ffc_update.update_trim(conn, trim_entity)
        
    except Exception as e:
        message = log_utils.write_exception(e)

# 入力値チェック
def _check(conn, trim_entity):
    
    # ファイルの長さ取得
    target_entity = ffc_select.get_target(conn, trim_entity.target_id)
    if (target_entity is None):
        return False
    file_duration_entity = ffc_add_files_sql.get_file_duration(conn, target_entity.file_id)
    video_stream = ffc_select.get_video_stream(conn, target_entity.file_id)
    
    # フレーム指定フラグチェック
    if (trim_entity.frame_input_flag and (video_stream is None)):
        return False
    
    # 時間・フレームを算出
    if (trim_entity.frame_input_flag):
        start_time, end_time = ffc_convert.frame_to_time(trim_entity.start_frame, trim_entity.end_frame, video_stream.video.r_frame_rate)
        trim_entity.start_time = start_time
        trim_entity.end_time = end_time
    else:
        if (video_stream is not None):
            start_frame, end_frame = ffc_convert.time_to_frame(trim_entity.start_time, trim_entity.end_time, video_stream.video.r_frame_rate)
            trim_entity.start_frame = start_frame
            trim_entity.end_frame = end_frame
    
    # トリム時間チェック
    if (0 > trim_entity.start_time):
        return False
    elif (trim_entity.start_time >= trim_entity.end_time):
        return False
    elif (trim_entity.end_time > file_duration_entity.duration):
        return False
    
    # トリムフレームチェック
    if (video_stream is not None):
        if (0 >= trim_entity.start_frame):
            return False
        elif (trim_entity.start_frame >= trim_entity.end_frame):
            return False
        elif (trim_entity.end_frame > file_duration_entity.nb_frames):
            return False
    
    # 映像フェードイン・アウトチェック
    trim_time = trim_entity.end_time - trim_entity.start_time
    if (trim_entity.video_fade_in < 0):
        return False
    elif (trim_entity.video_fade_out < 0):
        return False
    elif ((trim_entity.video_fade_in + trim_entity.video_fade_out) > trim_time):
        return False
    
    # 音声フェードイン・アウトチェック
    if (trim_entity.audio_fade_in < 0):
        return False
    elif (trim_entity.audio_fade_out < 0):
        return False
    elif ((trim_entity.audio_fade_in + trim_entity.audio_fade_out) > trim_time):
        return False
    
    return True

