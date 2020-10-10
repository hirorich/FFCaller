# ==================================================
# 作業用のエンティティ
# ==================================================

# ファイルの長さエンティティ
class FileDurationEntity():
    def __init__(self):
        self.__file_id = None
        self.__duration = 0.0
        self.__nb_frames = 0
    
    @property
    def file_id(self):
        return self.__file_id
    @file_id.setter
    def file_id(self, file_id):
        self.__file_id = int(file_id)
    
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = float(duration)
    
    @property
    def nb_frames(self):
        return self.__nb_frames
    @nb_frames.setter
    def nb_frames(self, nb_frames):
        self.__nb_frames = int(nb_frames)
