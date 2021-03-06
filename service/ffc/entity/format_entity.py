# ==================================================
# ffc_dbのエンティティ
# ==================================================

# フォーマットエンティティ
class FormatEntity():
    def __init__(self):
        self.__file_id = None
        self.__nb_streams = None
        self.__duration = None
        self.__size = None
    
    @property
    def file_id(self):
        return self.__file_id
    @file_id.setter
    def file_id(self, file_id):
        self.__file_id = int(file_id)
    
    @property
    def nb_streams(self):
        return self.__nb_streams
    @nb_streams.setter
    def nb_streams(self, nb_streams):
        self.__nb_streams = int(nb_streams)
    
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = float(duration)
    
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        self.__size = int(size)
    
    def to_dict(self):
        result = dict()
        result['file_id'] = self.__file_id
        result['nb_streams'] = self.__nb_streams
        result['duration'] = self.__duration
        result['size'] = self.__size
        return result
