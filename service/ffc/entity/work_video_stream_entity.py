# ==================================================
# 作業用のエンティティ
# ==================================================

# 映像ストリームエンティティ
class VideoStreamEntity():
    def __init__(self):
        self.__stream = None
        self.__video = None
    
    @property
    def stream(self):
        return self.__stream
    @stream.setter
    def stream(self, stream):
        self.__stream = stream
    
    @property
    def video(self):
        return self.__video
    @video.setter
    def video(self, video):
        self.__video = video
    
    def to_dict(self):
        result = dict()
        result['stream'] = self.__stream.to_dict()
        result['video'] = self.__video.to_dict()
        return result
