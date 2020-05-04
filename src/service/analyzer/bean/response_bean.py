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
    @property
    def video_stream_bean(self):
        return self.__video_stream_bean
    @video_stream_bean.setter
    def video_stream_bean(self, video_stream_bean):
        self.__video_stream_bean = video_stream_bean
    
    # オーディオストリームBeanリスト
    @property
    def audio_stream_bean_list(self):
        return self.__audio_stream_bean_list
    @audio_stream_bean_list.setter
    def audio_stream_bean_list(self, audio_stream_bean_list):
        self.__audio_stream_bean_list = audio_stream_bean_list
    
    # フォーマットBean
    @property
    def format_bean(self):
        return self.__format_bean
    @format_bean.setter
    def format_bean(self, format_bean):
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
    @property
    def index(self):
        return self.__index
    @index.setter
    def index(self, index):
        self.__index = index
    
    # コーデックタイプ
    @property
    def codec_type(self):
        return self.__codec_type
    @codec_type.setter
    def codec_type(self, codec_type):
        self.__codec_type = codec_type
    
    # コーデック名_略称
    @property
    def codec_name(self):
        return self.__codec_name
    @codec_name.setter
    def codec_name(self, codec_name):
        self.__codec_name = codec_name
    
    # コーデック名
    @property
    def codec_long_name(self):
        return self.__codec_long_name
    @codec_long_name.setter
    def codec_long_name(self, codec_long_name):
        self.__codec_long_name = codec_long_name
    
    # 長さ
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = duration
    
    # ビットレート
    @property
    def bit_rate(self):
        return self.__bit_rate
    @bit_rate.setter
    def bit_rate(self, bit_rate):
        self.__bit_rate = bit_rate
    
    # フレーム幅
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width
    
    # フレーム高
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height
    
    # fps
    @property
    def r_frame_rate(self):
        return self.__r_frame_rate
    @r_frame_rate.setter
    def r_frame_rate(self, r_frame_rate):
        self.__r_frame_rate = r_frame_rate
    
    # 総フレーム数
    @property
    def nb_frames(self):
        return self.__nb_frames
    @nb_frames.setter
    def nb_frames(self, nb_frames):
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
    @property
    def index(self):
        return self.__index
    @index.setter
    def index(self, index):
        self.__index = index
    
    # コーデックタイプ
    @property
    def codec_type(self):
        return self.__codec_type
    @codec_type.setter
    def codec_type(self, codec_type):
        self.__codec_type = codec_type
    
    # コーデック名_略称
    @property
    def codec_name(self):
        return self.__codec_name
    @codec_name.setter
    def codec_name(self, codec_name):
        self.__codec_name = codec_name
    
    # コーデック名
    @property
    def codec_long_name(self):
        return self.__codec_long_name
    @codec_long_name.setter
    def codec_long_name(self, codec_long_name):
        self.__codec_long_name = codec_long_name
    
    # 長さ
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = duration
    
    # ビットレート
    @property
    def bit_rate(self):
        return self.__bit_rate
    @bit_rate.setter
    def bit_rate(self, bit_rate):
        self.__bit_rate = bit_rate
    
    # サンプリング周波数
    @property
    def sample_rate(self):
        return self.__sample_rate
    @sample_rate.setter
    def sample_rate(self, sample_rate):
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
    @property
    def filename(self):
        return self.__filename
    @filename.setter
    def filename(self, filename):
        self.__filename = filename
    
    # ストリーム数
    @property
    def nb_streams(self):
        return self.__nb_streams
    @nb_streams.setter
    def nb_streams(self, nb_streams):
        self.__nb_streams = nb_streams
    
    # 長さ
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = duration
    
    # ファイルサイズ
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        self.__size = size
    
    # 辞書型に変換
    def parse_to_dict(self):
        bean_dict = dict()
        bean_dict['filename'] = self.__filename
        bean_dict['nb_streams'] = self.__nb_streams
        bean_dict['duration'] = self.__duration
        bean_dict['size'] = self.__size
        
        return bean_dict

