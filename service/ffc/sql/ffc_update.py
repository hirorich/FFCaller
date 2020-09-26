# ==================================================
# ffc_dbのデータ更新
# ==================================================

from common.utility import sqlite3_utils

# Trim更新
def update_trim(conn, trim_entity):
    query = []
    query.append(r'update Trim')
    query.append(r'set')
    query.append(r'start_time = ?,')
    query.append(r'end_time = ?,')
    query.append(r'start_frame = ?,')
    query.append(r'end_frame = ?,')
    query.append(r'frame_input_flag = ?,')
    query.append(r'video_fade_in = ?,')
    query.append(r'video_fade_out = ?,')
    query.append(r'audio_fade_in = ?,')
    query.append(r'audio_fade_out = ?')
    query.append(r'where')
    query.append(r'target_id = ?')
    param = (trim_entity.start_time, trim_entity.end_time, trim_entity.start_frame, trim_entity.end_frame, trim_entity.frame_input_flag, trim_entity.video_fade_in, trim_entity.video_fade_out, trim_entity.audio_fade_in, trim_entity.audio_fade_out, trim_entity.target_id)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)
