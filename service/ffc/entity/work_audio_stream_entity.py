# ==================================================
# 作業用のエンティティ
# ==================================================

# 音声ストリームエンティティ
class AudioStreamEntity():
    def __init__(self):
        self.__stream = None
        self.__audio = None
    
    @property
    def stream(self):
        return self.__stream
    @stream.setter
    def stream(self, stream):
        self.__stream = stream
    
    @property
    def audio(self):
        return self.__audio
    @audio.setter
    def audio(self, audio):
        self.__audio = audio
    
    def to_dict(self):
        result = dict()
        result['stream'] = self.__stream.to_dict()
        result['audio'] = self.__audio.to_dict()
        return result
