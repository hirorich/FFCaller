# ==================================================
# ffc_dbのデータ追加
# ==================================================

from common.utility import sqlite3_utils

# Target追加
def insert_target(conn, target_entity):
    query = []
    query.append(r'insert into Target')
    query.append(r'(target_id, file_id, item_order)')
    query.append(r'VALUES')
    query.append(r'(?, ?, ?)')
    param = (target_entity.target_id, target_entity.file_id, target_entity.item_order)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Trim追加
def insert_trim(conn, trim_entity):
    query = []
    query.append(r'insert into Trim')
    query.append(r'(target_id, start_time, end_time, start_frame, end_frame, frame_input_flag, video_fade_in, video_fade_out, audio_fade_in, audio_fade_out, is_fade_from_white, is_fade_to_white)')
    query.append(r'VALUES')
    query.append(r'(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
    param = (trim_entity.target_id, trim_entity.start_time, trim_entity.end_time, trim_entity.start_frame, trim_entity.end_frame, trim_entity.frame_input_flag, trim_entity.video_fade_in, trim_entity.video_fade_out, trim_entity.audio_fade_in, trim_entity.audio_fade_out, trim_entity.is_fade_from_white, trim_entity.is_fade_to_white)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# File追加
def insert_file(conn, file_entity):
    query = []
    query.append(r'insert into File')
    query.append(r'(file_id, filename, filepath, workpath, webpath)')
    query.append(r'VALUES')
    query.append(r'(?, ?, ?, ?, ?)')
    param = (file_entity.file_id, file_entity.filename, file_entity.filepath, file_entity.workpath, file_entity.webpath)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Format追加
def insert_format(conn, format_entity):
    query = []
    query.append(r'insert into Format')
    query.append(r'(file_id, nb_streams, duration, size)')
    query.append(r'VALUES')
    query.append(r'(?, ?, ?, ?)')
    param = (format_entity.file_id, format_entity.nb_streams, format_entity.duration, format_entity.size)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Stream追加
def insert_stream(conn, stream_entity):
    query = []
    query.append(r'insert into Stream')
    query.append(r'(file_id, stream_index, codec_type, codec_name, codec_long_name, duration, bit_rate)')
    query.append(r'VALUES')
    query.append(r'(?, ?, ?, ?, ?, ?, ?)')
    param = (stream_entity.file_id, stream_entity.stream_index, stream_entity.codec_type, stream_entity.codec_name, stream_entity.codec_long_name, stream_entity.duration, stream_entity.bit_rate)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Video追加
def insert_video(conn, video_entity):
    query = []
    query.append(r'insert into Video')
    query.append(r'(file_id, stream_index, width, height, r_frame_rate, nb_frames)')
    query.append(r'VALUES')
    query.append(r'(?, ?, ?, ?, ?, ?)')
    param = (video_entity.file_id, video_entity.stream_index, video_entity.width, video_entity.height, video_entity.r_frame_rate, video_entity.nb_frames)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)

# Audio追加
def insert_audio(conn, audio_entity):
    query = []
    query.append(r'insert into Audio')
    query.append(r'(file_id, stream_index, sample_rate)')
    query.append(r'VALUES')
    query.append(r'(?, ?, ?)')
    param = (audio_entity.file_id, audio_entity.stream_index, audio_entity.sample_rate)
    
    sqlite3_utils.execute(conn, ' '.join(query), param)
