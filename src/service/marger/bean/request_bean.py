# ==================================================
# 動画変換リクエストBean
# ==================================================

# ==================================================
# 動画変換リクエストBean
# ==================================================
class MargerRequestBean:
    
    def __init__(self):
        self.__input_file_bean_list = []
        self.__output_file_bean = None
        
    
    # 入力ファイルBeanリスト
    def get_input_file_bean_list(self):
        return self.__input_file_bean_list
    def set_input_file_bean_list(self, input_file_bean_list):
        self.__input_file_bean_list = input_file_bean_list
    
    # 出力ファイルBean
    def get_output_file_bean(self):
        return self.__output_file_bean
    def set_output_file_bean(self, output_file_bean):
        self.__output_file_bean = output_file_bean

# ==================================================
# 動画変換入力ファイルBean
# ==================================================
class MargerInputFileBean:
    
    def __init__(self):
        self.__input_file_name = ''
        self.__start_time = 0
        self.__trim_duration = 0
        self.__start_frame = 1
        self.__frame_number = 1
        self.__frame_specification_flag = False
        
        self.__video_fade_in_duration = 0
        self.__video_fade_out_duration = 0
        self.__audio_fade_in_duration = 0
        self.__audio_fade_out_duration = 0
        
    
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
    
    # 開始フレーム
    def get_start_frame(self):
        return self.__start_frame
    def set_start_frame(self, start_frame):
        self.__start_frame = start_frame
    
    # フレーム数
    def get_frame_number(self):
        return self.__frame_number
    def set_frame_number(self, frame_number):
        self.__frame_number = frame_number
    
    # フレーム指定フラグ
    def get_frame_specification_flag(self):
        return self.__frame_specification_flag
    def set_frame_specification_flag(self, frame_specification_flag):
        self.__frame_specification_flag = frame_specification_flag
    
    # 映像フェードイン期間
    def get_video_fade_in_duration(self):
        return self.__video_fade_in_duration
    def set_video_fade_in_duration(self, video_fade_in_duration):
        self.__video_fade_in_duration = video_fade_in_duration
    
    # 映像フェードアウト期間
    def get_video_fade_out_duration(self):
        return self.__video_fade_out_duration
    def set_video_fade_out_duration(self, video_fade_out_duration):
        self.__video_fade_out_duration = video_fade_out_duration
    
    # 音声フェードイン期間
    def get_audio_fade_in_duration(self):
        return self.__audio_fade_in_duration
    def set_audio_fade_in_duration(self, audio_fade_in_duration):
        self.__audio_fade_in_duration = audio_fade_in_duration
    
    # 音声フェードアウト期間
    def get_audio_fade_out_duration(self):
        return self.__audio_fade_out_duration
    def set_audio_fade_out_duration(self, audio_fade_out_duration):
        self.__audio_fade_out_duration = audio_fade_out_duration

# ==================================================
# 動画変換出力ファイルBean
# ==================================================
class MargerOutputFileBean:
    
    def __init__(self):
        self.__overwriting_flag = True
        self.__output_file_name = ''
        self.__codec_type_combination = 1
        
    
    # 上書きフラグ
    def get_overwriting_flag(self):
        return self.__overwriting_flag
    def set_overwriting_flag(self, overwriting_flag):
        self.__overwriting_flag = overwriting_flag
    
    # 出力ファイル名
    def get_output_file_name(self):
        return self.__output_file_name
    def set_output_file_name(self, output_file_name):
        self.__output_file_name = output_file_name
    
    # コーデックタイプ組み合わせ
    def get_codec_type_combination(self):
        return self.__codec_type_combination
    def set_codec_type_combination(self, codec_type_combination):
        self.__codec_type_combination = codec_type_combination

