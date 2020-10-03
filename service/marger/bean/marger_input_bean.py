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
    
    def trim_duration(self):
        return self.__end_time - self.__start_time
    
    def create_input_list(self):
        command = []
        command.append("-ss")
        command.append(str(self.__start_time))
        command.append("-t")
        command.append(str(self.trim_duration()))
        command.append("-i")
        command.append(self.__workpath)
        return command
    
    def create_filter_list(self, file_index):
        index = str(file_index)
        video_filter = []
        audio_filter = []
        video_id = r'[' + index + r':v]'
        audio_id = r'[' + index + r':a]'
        
        if self.__with_video:
            id_count = 0
            if self.__video_fade_in > 0:
                work_id = index + 'v' + str(id_count)
                video_filter.append(video_id + 'fade=t=in:st=0:d=' + str(self.__video_fade_in) + work_id)
                video_id = work_id
                id_count += 1
            if self.__video_fade_out > 0:
                work_id = index + 'v' + str(id_count)
                video_filter.append(video_id + 'fade=t=out:st=' + str(self.trim_duration() - self.__video_fade_out) + ':d=' + str(self.__video_fade_out) + work_id)
                video_id = work_id
                id_count += 1
        
        if self.__with_audio:
            id_count = 0
            if self.__audio_fade_in > 0:
                work_id = index + 'a' + str(id_count)
                audio_filter.append(audio_id + 'afade=t=in:st=0:d=' + str(self.__audio_fade_in) + work_id)
                audio_id = work_id
                id_count += 1
            if self.__audio_fade_out > 0:
                work_id = index + 'a' + str(id_count)
                audio_filter.append(audio_id + 'afade=t=out:st=' + str(self.trim_duration() - self.__audio_fade_out) + ':d=' + str(self.__audio_fade_out) + work_id)
                audio_id = work_id
                id_count += 1
        
        filter = []
        filter.extend(video_filter)
        filter.extend(audio_filter)
        
        return filter, video_id, audio_id
