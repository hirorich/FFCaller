# ==================================================
# 動画結合作業用のビーン
# ==================================================

# 入力ターゲットビーン
class MargerInputBean():
    def __init__(self):
        self.__workpath = None
        self.__start_time = 0.0
        self.__end_time = 0.0
        self.__video_fade_in = 0.0
        self.__video_fade_out = 0.0
        self.__audio_fade_in = 0.0
        self.__audio_fade_out = 0.0
        self.__with_video = False
        self.__with_audio = False
    
    @property
    def workpath(self):
        return self.__workpath
    @workpath.setter
    def workpath(self, workpath):
        self.__workpath = str(workpath)
    
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
    def video_fade_in(self):
        return self.__video_fade_in
    @video_fade_in.setter
    def video_fade_in(self, video_fade_in):
        self.__video_fade_in = float(video_fade_in)
    
    @property
    def video_fade_out(self):
        return self.__video_fade_out
    @video_fade_out.setter
    def video_fade_out(self, video_fade_out):
        self.__video_fade_out = float(video_fade_out)
    
    @property
    def audio_fade_in(self):
        return self.__audio_fade_in
    @audio_fade_in.setter
    def audio_fade_in(self, audio_fade_in):
        self.__audio_fade_in = float(audio_fade_in)
    
    @property
    def audio_fade_out(self):
        return self.__audio_fade_out
    @audio_fade_out.setter
    def audio_fade_out(self, audio_fade_out):
        self.__audio_fade_out = float(audio_fade_out)
    
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
