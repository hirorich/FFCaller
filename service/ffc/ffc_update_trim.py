# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

from common import app_property
from common.utility import log_utils
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
        return false
    file_duration_entity = ffc_add_files_sql.get_file_duration(conn, target_entity.file_id)
    video_stream = ffc_select.get_video_stream(conn, target_entity.file_id)
    
    # トリム時間チェック
    if (0 > trim_entity.start_time):
        return false
    elif (trim_entity.start_time > trim_entity.end_time):
        return false
    elif (trim_entity.end_time > file_duration_entity.duration):
        return false
    
    # トリムフレームチェック
    if (video_stream is not None):
        if (0 >= trim_entity.start_frame):
            return false
        elif (trim_entity.start_frame > trim_entity.end_frame):
            return false
        elif (trim_entity.end_frame > file_duration_entity.nb_frames):
            return false
    
    # フレーム指定フラグチェック
    if (trim_entity.frame_input_flag and (video_stream is None)):
        return false
    
    # フェードイン・アウトチェック準備
    trim_time = 0
    if (trim_entity.frame_input_flag):
        r_frame_rate = video_stream.video.r_frame_rate.split('/')
        r_frame_rate_numer = int(r_frame_rate[0])
        r_frame_rate_denom = int(r_frame_rate[1])
        start_time = (trim_entity.start_frame - 1) * r_frame_rate_denom / r_frame_rate_numer
        end_time = trim_entity.end_frame * r_frame_rate_denom / r_frame_rate_numer
        trim_time = end_time - start_time
    else:
        trim_time = trim_entity.end_time - trim_entity.start_time
    
    # 映像フェードイン・アウトチェック
    if (trim_entity.video_fade_in < 0):
        return false
    elif (trim_entity.video_fade_out < 0):
        return false
    elif ((trim_entity.video_fade_in + trim_entity.video_fade_out) > trim_time):
        return false
    
    # 音声フェードイン・アウトチェック
    if (trim_entity.audio_fade_in < 0):
        return false
    elif (trim_entity.audio_fade_out < 0):
        return false
    elif ((trim_entity.audio_fade_in + trim_entity.audio_fade_out) > trim_time):
        return false
    
    return true

