# ==================================================
# ffc_dbのエンティティ
# ==================================================

# 音声エンティティ
class AudioEntity():
    def __init__(self):
        self.__file_id = None
        self.__stream_index = None
        self.__sample_rate = None
    
    @property
    def file_id(self):
        return self.__file_id
    @file_id.setter
    def file_id(self, file_id):
        self.__file_id = int(file_id)
    
    @property
    def stream_index(self):
        return self.__stream_index
    @stream_index.setter
    def stream_index(self, stream_index):
        self.__stream_index = int(stream_index)
    
    @property
    def sample_rate(self):
        return self.__sample_rate
    @sample_rate.setter
    def sample_rate(self, sample_rate):
        self.__sample_rate = int(sample_rate)
    
    def to_dict(self):
        result = dict()
        result['file_id'] = self.__file_id
        result['stream_index'] = self.__stream_index
        result['sample_rate'] = self.__sample_rate
        return result
