# ==================================================
# 動画結合作業用のビーン
# ==================================================

# 出力ターゲットビーン
class MargerOutputBean():
    def __init__(self):
        self.__filepath = None
        self.__with_video = False
        self.__with_audio = False
        self.__input_beans = []
    
    @property
    def filepath(self):
        return self.__filepath
    @filepath.setter
    def filepath(self, filepath):
        self.__filepath = str(filepath)
    
    @property
    def with_video(self):
        return self.__with_video
    @with_video.setter
    def with_video(self, with_video):
        self.__with_video = bool(with_video)
    
    @property
    def with_audio(self):
        return self.__with_audio
    @with_audio.setter
    def with_audio(self, with_audio):
        self.__with_audio = bool(with_audio)
    
    def append_input_bean(self, input_bean):
        self.__input_beans.append(input_bean)
    def get_input_bean_list(self):
        return self.__input_beans
