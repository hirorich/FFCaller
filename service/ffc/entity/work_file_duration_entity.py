# ==================================================
# 作業用のエンティティ
# ==================================================

# ファイルの長さエンティティ
class FileDurationEntity():
    def __init__(self):
        self.__file_id = None
        self.__trim_duration = 0.0
        self.__nb_frames = 0
    
    @property
    def file_id(self):
        return self.__file_id
    @file_id.setter
    def file_id(self, file_id):
        self.__file_id = int(file_id)
    
    @property
    def trim_duration(self):
        return self.__trim_duration
    @trim_duration.setter
    def trim_duration(self, trim_duration):
        self.__trim_duration = float(trim_duration)
    
    @property
    def nb_frames(self):
        return self.__nb_frames
    @nb_frames.setter
    def nb_frames(self, nb_frames):
        self.__nb_frames = int(nb_frames)
