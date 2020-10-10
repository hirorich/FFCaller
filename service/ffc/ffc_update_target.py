# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

from service.ffc.sql import ffc_update

# 並び順更新実行
def update_order(conn, input_target_bean_list):
    
    new_order = 0
    for input_target in input_target_bean_list:
        
        # 並び順更新
        ffc_update.update_target_order(conn, input_target.target_id, new_order)
        new_order += 1
