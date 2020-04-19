# ==================================================
# 動画解析レスポンスBean
# ==================================================

# ==================================================
# 動画解析レスポンスBean
# ==================================================
class AnalyzerResponseBean:
    
    def __init__(self):
        self.__video_stream_bean = None
        self.__audio_stream_bean_list = None
        self.__format_bean = None
        
    
    # ビデオストリームBean
    def get_video_stream_bean(self):
        return self.__video_stream_bean
    def set_video_stream_bean(self, video_stream_bean):
        self.__video_stream_bean = video_stream_bean
    
    # オーディオストリームBeanリスト
    def get_audio_stream_bean_list(self):
        return self.__audio_stream_bean_list
    def set_audio_stream_bean_list(self, audio_stream_bean_list):
        self.__audio_stream_bean_list = audio_stream_bean_list
    
    # フォーマットBean
    def get_format_bean(self):
        return self.__format_bean
    def set_format_bean(self, format_bean):
        self.__format_bean = format_bean
    
    # 辞書型に変換
    def parse_to_dict(self):
        bean_dict = dict()
        if self.__video_stream_bean is not None:
            bean_dict['video'] = self.__video_stream_bean.parse_to_dict()
        
        if self.__audio_stream_bean_list is not None:
            if len(self.__audio_stream_bean_list) != 0:
                audio_bean_list = []
                for audio_bean in self.__audio_stream_bean_list:
                    audio_bean_list.append(audio_bean.parse_to_dict())
                
                bean_dict['audio'] = audio_bean_list
        
        if self.__video_stream_bean is not None:
            bean_dict['format'] = self.__format_bean.parse_to_dict()
        
        return bean_dict
    

# ==================================================
# 動画解析ビデオストリームBean
# ==================================================
class AnalyzerVideoStreamBean:
    
    def __init__(self):
        self.__index = 0
        self.__codec_type = ''
        self.__codec_name = ''
        self.__codec_long_name = ''
        self.__duration = ''
        self.__bit_rate = ''
        self.__width = 0
        self.__height = 0
        self.__r_frame_rate = ''
        self.__nb_frames = ''
        
    
    # インデックス
    def get_index(self):
        return self.__index
    def set_index(self, index):
        self.__index = index
    
    # コーデックタイプ
    def get_codec_type(self):
        return self.__codec_type
    def set_codec_type(self, codec_type):
        self.__codec_type = codec_type
    
    # コーデック名_略称
    def get_codec_name(self):
        return self.__codec_name
    def set_codec_name(self, codec_name):
        self.__codec_name = codec_name
    
    # コーデック名
    def get_codec_long_name(self):
        return self.__codec_long_name
    def set_codec_long_name(self, codec_long_name):
        self.__codec_long_name = codec_long_name
    
    # 長さ
    def get_duration(self):
        return self.__duration
    def set_duration(self, duration):
        self.__duration = duration
    
    # ビットレート
    def get_bit_rate(self):
        return self.__bit_rate
    def set_bit_rate(self, bit_rate):
        self.__bit_rate = bit_rate
    
    # フレーム幅
    def get_width(self):
        return self.__width
    def set_width(self, width):
        self.__width = width
    
    # フレーム高
    def get_height(self):
        return self.__height
    def set_height(self, height):
        self.__height = height
    
    # fps
    def get_r_frame_rate(self):
        return self.__r_frame_rate
    def set_r_frame_rate(self, r_frame_rate):
        self.__r_frame_rate = r_frame_rate
    
    # 総フレーム数
    def get_nb_frames(self):
        return self.__nb_frames
    def set_nb_frames(self, nb_frames):
        self.__nb_frames = nb_frames
    
    # 辞書型に変換
    def parse_to_dict(self):
        bean_dict = dict()
        bean_dict['index'] = self.__index
        bean_dict['codec_type'] = self.__codec_type
        bean_dict['codec_name'] = self.__codec_name
        bean_dict['codec_long_name'] = self.__codec_long_name
        bean_dict['duration'] = self.__duration
        bean_dict['bit_rate'] = self.__bit_rate
        bean_dict['width'] = self.__width
        bean_dict['height'] = self.__height
        bean_dict['r_frame_rate'] = self.__r_frame_rate
        bean_dict['nb_frames'] = self.__nb_frames
        
        return bean_dict
    

# ==================================================
# 動画解析オーディオストリームBean
# ==================================================
class AnalyzerAudioStreamBean:
    
    def __init__(self):
        self.__index = 0
        self.__codec_type = ''
        self.__codec_name = ''
        self.__codec_long_name = ''
        self.__duration = ''
        self.__bit_rate = ''
        self.__sample_rate = ''
        
    
    # インデックス
    def get_index(self):
        return self.__index
    def set_index(self, index):
        self.__index = index
    
    # コーデックタイプ
    def get_codec_type(self):
        return self.__codec_type
    def set_codec_type(self, codec_type):
        self.__codec_type = codec_type
    
    # コーデック名_略称
    def get_codec_name(self):
        return self.__codec_name
    def set_codec_name(self, codec_name):
        self.__codec_name = codec_name
    
    # コーデック名
    def get_codec_long_name(self):
        return self.__codec_long_name
    def set_codec_long_name(self, codec_long_name):
        self.__codec_long_name = codec_long_name
    
    # 長さ
    def get_duration(self):
        return self.__duration
    def set_duration(self, duration):
        self.__duration = duration
    
    # ビットレート
    def get_bit_rate(self):
        return self.__bit_rate
    def set_bit_rate(self, bit_rate):
        self.__bit_rate = bit_rate
    
    # サンプリング周波数
    def get_sample_rate(self):
        return self.__sample_rate
    def set_sample_rate(self, sample_rate):
        self.__sample_rate = sample_rate
    
    # 辞書型に変換
    def parse_to_dict(self):
        bean_dict = dict()
        bean_dict['index'] = self.__index
        bean_dict['codec_type'] = self.__codec_type
        bean_dict['codec_name'] = self.__codec_name
        bean_dict['codec_long_name'] = self.__codec_long_name
        bean_dict['duration'] = self.__duration
        bean_dict['bit_rate'] = self.__bit_rate
        bean_dict['sample_rate'] = self.__sample_rate
        
        return bean_dict
        

# ==================================================
# 動画解析フォーマットBean
# ==================================================
class AnalyzerFormatBean:
    
    def __init__(self):
        self.__filename = ''
        self.__nb_streams = 0
        self.__duration = ''
        self.__size = ''
        
    
    # ファイル名
    def get_filename(self):
        return self.__filename
    def set_filename(self, filename):
        self.__filename = filename
    
    # ストリーム数
    def get_nb_streams(self):
        return self.__nb_streams
    def set_nb_streams(self, nb_streams):
        self.__nb_streams = nb_streams
    
    # 長さ
    def get_duration(self):
        return self.__duration
    def set_duration(self, duration):
        self.__duration = duration
    
    # ファイルサイズ
    def get_size(self):
        return self.__size
    def set_size(self, size):
        self.__size = size
    
    # 辞書型に変換
    def parse_to_dict(self):
        bean_dict = dict()
        bean_dict['filename'] = self.__filename
        bean_dict['nb_streams'] = self.__nb_streams
        bean_dict['duration'] = self.__duration
        bean_dict['size'] = self.__size
        
        return bean_dict
        

