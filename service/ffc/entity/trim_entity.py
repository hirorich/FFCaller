# ==================================================
# ffc_dbのエンティティ
# ==================================================

# トリムエンティティ
class TrimEntity():
    def __init__(self):
        self.__target_id = None
        self.__start_time = 0.0
        self.__end_time = 0.0
        self.__start_frame = 0
        self.__end_frame = 0
        self.__frame_input_flag = False
        self.__video_fade_in = 0.0
        self.__video_fade_out = 0.0
        self.__audio_fade_in = 0.0
        self.__audio_fade_out = 0.0
    
    @property
    def target_id(self):
        return self.__target_id
    @target_id.setter
    def target_id(self, target_id):
        self.__target_id = int(target_id)
    
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
    def start_frame(self):
        return self.__start_frame
    @start_frame.setter
    def start_frame(self, start_frame):
        self.__start_frame = int(start_frame)
    
    @property
    def end_frame(self):
        return self.__end_frame
    @end_frame.setter
    def end_frame(self, end_frame):
        self.__end_frame = int(end_frame)
    
    @property
    def frame_input_flag(self):
        return self.__frame_input_flag
    @frame_input_flag.setter
    def frame_input_flag(self, frame_input_flag):
        self.__frame_input_flag = bool(frame_input_flag)
    
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
    
    def to_dict(self):
        result = dict()
        result['target_id'] = self.__target_id
        result['start_time'] = self.__start_time
        result['end_time'] = self.__end_time
        result['start_frame'] = self.__start_frame
        result['end_frame'] = self.__end_frame
        result['frame_input_flag'] = self.__frame_input_flag
        result['video_fade_in'] = self.__video_fade_in
        result['video_fade_out'] = self.__video_fade_out
        result['audio_fade_in'] = self.__audio_fade_in
        result['audio_fade_out'] = self.__audio_fade_out
        return result
