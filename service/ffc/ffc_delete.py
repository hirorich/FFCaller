# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

from common import app_property
from common.utility import file_utils, log_utils
from service.common.const import env_const
from service.ffc.sql import ffc_delete, ffc_select

# ターゲット削除削除
def delete_target(conn, target_id):
    try:
        # ターゲット削除
        target_entity = ffc_select.get_target(conn, target_id)
        ffc_delete.delete_trim(conn, target_id)
        ffc_delete.delete_target(conn, target_id)
        
        # ファイル削除
        if len(ffc_select.get_targets_by_file_id(conn, target_entity.file_id)) == 0:
            file_entity = ffc_select.get_file(conn, target_entity.file_id)
            if file_utils.delete_file(file_entity.workpath):
                ffc_delete.delete_format(conn, target_entity.file_id)
                ffc_delete.delete_video(conn, target_entity.file_id)
                ffc_delete.delete_audio(conn, target_entity.file_id)
                ffc_delete.delete_stream(conn, target_entity.file_id)
                ffc_delete.delete_file(conn, target_entity.file_id)
        
    except Exception as e:
        message = log_utils.write_exception(e)

# 全削除
def delete_all(conn):
    try:
        # ファイル削除
        for filepath in list(env_const.WORK_DIR.iterdir()):
            file_utils.delete_file(str(filepath))
        
        # 全テーブル削除
        ffc_delete.delete_format_all(conn)
        ffc_delete.delete_video_all(conn)
        ffc_delete.delete_audio_all(conn)
        ffc_delete.delete_stream_all(conn)
        ffc_delete.delete_file_all(conn)
        ffc_delete.delete_trim_all(conn)
        ffc_delete.delete_target_all(conn)
        
    except Exception as e:
        message = log_utils.write_exception(e)
