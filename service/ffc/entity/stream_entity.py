# ==================================================
# ffc_dbのエンティティ
# ==================================================

# ストリームエンティティ
class StreamEntity():
    def __init__(self):
        self.__file_id = None
        self.__stream_index = None
        self.__codec_type = None
        self.__codec_name = None
        self.__codec_long_name = None
        self.__duration = None
        self.__bit_rate = None
    
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
    def codec_type(self):
        return self.__codec_type
    @codec_type.setter
    def codec_type(self, codec_type):
        self.__codec_type = codec_type
    
    @property
    def codec_name(self):
        return self.__codec_name
    @codec_name.setter
    def codec_name(self, codec_name):
        self.__codec_name = codec_name
    
    @property
    def codec_long_name(self):
        return self.__codec_long_name
    @codec_long_name.setter
    def codec_long_name(self, codec_long_name):
        self.__codec_long_name = codec_long_name
    
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = float(duration)
    
    @property
    def bit_rate(self):
        return self.__bit_rate
    @bit_rate.setter
    def bit_rate(self, bit_rate):
        self.__bit_rate = int(bit_rate)
