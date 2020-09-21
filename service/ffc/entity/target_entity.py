# ==================================================
# ffc_dbのエンティティ
# ==================================================

# ターゲットエンティティ
class TargetEntity():
    def __init__(self):
        self.__target_id = None
        self.__file_id = None
        self.__item_order = None
    
    @property
    def target_id(self):
        return self.__target_id
    @target_id.setter
    def target_id(self, target_id):
        self.__target_id = int(target_id)
    
    @property
    def file_id(self):
        return self.__file_id
    @file_id.setter
    def file_id(self, file_id):
        self.__file_id = int(file_id)
    
    @property
    def item_order(self):
        return self.__item_order
    @item_order.setter
    def item_order(self, item_order):
        self.__item_order = int(item_order)
