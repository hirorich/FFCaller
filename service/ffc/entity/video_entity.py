# ==================================================
# ffc_dbのエンティティ
# ==================================================

# 映像エンティティ
class VideoEntity():
    def __init__(self):
        self.__file_id = None
        self.__stream_index = None
        self.__width = None
        self.__height = None
        self.__r_frame_rate = None
        self.__nb_frames = None
    
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
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = int(width)
    
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = int(height)
    
    @property
    def r_frame_rate(self):
        return self.__r_frame_rate
    @r_frame_rate.setter
    def r_frame_rate(self, r_frame_rate):
        self.__r_frame_rate = r_frame_rate
    
    @property
    def nb_frames(self):
        return self.__nb_frames
    @nb_frames.setter
    def nb_frames(self, nb_frames):
        self.__nb_frames = int(nb_frames)
