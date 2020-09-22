# ==================================================
# 作業用のエンティティ
# ==================================================

# 入力ターゲットエンティティ
class InputTargetEntity():
    def __init__(self):
        self.__target_id = None
        self.__filename = None
        self.__filepath = None
        self.__start_time = 0.0
        self.__end_time = 0.0
        self.__item_order = None
    
    @property
    def target_id(self):
        return self.__target_id
    @target_id.setter
    def target_id(self, target_id):
        self.__target_id = int(target_id)
    
    @property
    def filename(self):
        return self.__filename
    @filename.setter
    def filename(self, filename):
        self.__filename = str(filename)
    
    @property
    def filepath(self):
        return self.__filepath
    @filepath.setter
    def filepath(self, filepath):
        self.__filepath = str(filepath)
    
    @property
    def start_time(self):
        return self.__start_time
    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = float(start_time)
    
    @property
    def end_time(self):
        return self.__end_time
    @end_time.setter
    def end_time(self, end_time):
        self.__end_time = float(end_time)
    
    @property
    def item_order(self):
        return self.__item_order
    @item_order.setter
    def item_order(self, item_order):
        self.__item_order = int(item_order)
    
    def to_dict(self):
        result = dict()
        result['target_id'] = self.__target_id
        result['filename'] = self.__filename
        result['filepath'] = self.__filepath
        result['start_time'] = self.__start_time
        result['end_time'] = self.__end_time
        result['item_order'] = self.__item_order
        return result
