# ==================================================
# ffc_dbの情報取得
# ==================================================

from common.utility import sqlite3_utils
from service.ffc.entity.audio_entity import AudioEntity
from service.ffc.entity.format_entity import FormatEntity
from service.ffc.entity.stream_entity import StreamEntity
from service.ffc.entity.video_entity import VideoEntity
from service.ffc.entity.work_input_target_entity import InputTargetEntity

# 入力ターゲットリスト取得
def get_input_target_list(conn):
    query = []
    query.append(r'select')
    query.append(r'Target.target_id, File.file_id, File.filename, File.filepath, Trim.start_time, Trim.trim_duration, Target.item_order')
    query.append(r'from Target')
    query.append(r'inner join Trim')
    query.append(r'on Target.target_id = Trim.target_id')
    query.append(r'inner join File')
    query.append(r'on Target.file_id = File.file_id')
    query.append(r'order by')
    query.append(r'Target.item_order, Target.target_id')
    
    result = []
    for input_target in sqlite3_utils.fetchall(conn, ' '.join(query)):
        entity = InputTargetEntity()
        entity.target_id = input_target[0]
        entity.file_id = input_target[1]
        entity.filename = input_target[2]
        entity.filepath = input_target[3]
        entity.start_time = input_target[4]
        entity.trim_duration = input_target[5]
        entity.item_order = input_target[6]
        result.append(entity)
    
    return result
