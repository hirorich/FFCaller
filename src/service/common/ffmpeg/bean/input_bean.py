# ==================================================
# ffmpeg入力部分Bean
# ==================================================

# ==================================================
# ffmpeg入力部分Bean
# ==================================================
class FFmpegInputBean:
    
    def __init__(self):
        self.__input_file_name = ''
        self.__start_time = 0
        self.__trim_duration = 0
        
        self.__filter_string = ''
        
        self.__filtered_video_id = ''
        self.__filtered_audio_id = ''
        
        self.__start_frame = 1
        
    
    # 入力ファイル名
    def get_input_file_name(self):
        return self.__input_file_name
    def set_input_file_name(self, input_file_name):
        self.__input_file_name = input_file_name
    
    # 開始時間
    def get_start_time(self):
        return self.__start_time
    def set_start_time(self, start_time):
        self.__start_time = start_time
    
    # 切り取り期間
    def get_trim_duration(self):
        return self.__trim_duration
    def set_trim_duration(self, trim_duration):
        self.__trim_duration = trim_duration
    
    # フィルター文字列
    def get_filter_string(self):
        return self.__filter_string
    def set_filter_string(self, filter_string):
        self.__filter_string = filter_string
    
    # フィルター後映像識別子
    def get_filtered_video_id(self):
        return self.__filtered_video_id
    def set_filtered_video_id(self, filtered_video_id):
        self.__filtered_video_id = filtered_video_id
    
    # フィルター後音声識別子
    def get_filtered_audio_id(self):
        return self.__filtered_audio_id
    def set_filtered_audio_id(self, filtered_audio_id):
        self.__filtered_audio_id = filtered_audio_id
    
    # 開始フレーム
    def get_start_frame(self):
        return self.__start_frame
    def set_start_frame(self, start_frame):
        self.__start_frame = start_frame
    
    
    
    # 
    def create_input_command(self):
        command = []
        command.append("-ss")
        command.append(str(self.__start_time))
        command.append("-t")
        command.append(str(self.__trim_duration))
        command.append("-i")
        command.append(self.__input_file_name)
        return command
    

