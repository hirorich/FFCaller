# ==================================================
# ffmpegを用いた動画変換コマンド生成
# ==================================================

from service.analyzer import analyzer_controller
from service.analyzer.bean.analyzer_request_bean import AnalyzerRequestBean
from service.converter.bean.command_bean import CommandInputBean
from service.common import file_utils
from service.common import fps_utils
from service.common.type import number_utils
from service.common.type import str_utils

# 
def create_command(request_bean):
    
    # === 入力チェック ===
    # ====================
    
    command = []
    
    for input_file_bean in request_bean.get_input_file_bean_list():
        print(input_file_bean.get_input_file_name())
        print(input_file_bean.get_start_time())
        print(input_file_bean.get_trim_duration())
        print(input_file_bean.get_start_frame())
        print(input_file_bean.get_frame_number())
        print(input_file_bean.get_frame_specification_flag())
        print(input_file_bean.get_video_fade_in_duration())
        print(input_file_bean.get_video_fade_out_duration())
        print(input_file_bean.get_audio_fade_in_duration())
        print(input_file_bean.get_audio_fade_out_duration())
        
        input_bean = create_input_bean(input_file_bean)
        print(input_bean.get_input_file_name())
        print(input_bean.get_start_time())
        print(input_bean.get_trim_duration())
        print(input_bean.get_start_frame())
        print(input_bean.create_input_command())
    
    output_file_bean = request_bean.get_output_file_bean()
    print(output_file_bean.get_convert_mode())
    print(output_file_bean.get_overwriting_flag())
    print(output_file_bean.get_output_file_name())
    print(output_file_bean.get_codec_type_combination())
    
    return command
    

def create_input_bean(input_file_bean):
    
    command_input_bean = CommandInputBean()
    
    # === 入力チェック ===
    # 入力ファイル名が空白
    input_file_name = input_file_bean.get_input_file_name()
    if str_utils.is_none_or_whitespace(input_file_name):
        raise Exception('"input_file" is not specified')
    
    # 入力ファイルが存在しない
    input_file_name = input_file_name.strip()
    if not file_utils.is_exists(input_file_name):
        raise Exception('"' + input_file_name + '" is not exists')
    
    # フレーム指定の場合、フレームは1以上を指定
    if input_file_bean.get_frame_specification_flag():
        if number_utils.is_less(input_file_bean.get_start_frame(), 1):
            raise Exception('"' + input_file_name + '": specify at least 1 for "start_frame"')
        
        if number_utils.is_less(input_file_bean.get_frame_number(), 1):
            raise Exception('"' + input_file_name + '": specify at least 1 for "frame_number"')
        
        # フレーム指定でない場合、時間は0以上を指定
    else:
        if number_utils.is_less(input_file_bean.get_start_time(), 0):
            raise Exception('"' + input_file_name + '": specify at least 0 for "start_time"')
        
        if number_utils.is_less(input_file_bean.get_trim_duration(), 0):
            raise Exception('"' + input_file_name + '": specify at least 0 for "trim_duration"')
    # ====================
    
    # 入力ファイル名指定
    command_input_bean.set_input_file_name(input_file_name)
    
    # 動画情報取得
    analyzer_request_bean = AnalyzerRequestBean()
    analyzer_request_bean.set_input_file_name(input_file_name)
    analyzer_response_bean = analyzer_controller.analize(analyzer_request_bean)
    format_bean = analyzer_response_bean.get_format_bean()
    video_stream_bean = analyzer_response_bean.get_video_stream_bean()
    audio_stream_bean_list = analyzer_response_bean.get_audio_stream_bean_list()
    print(video_stream_bean.get_r_frame_rate())
    
    # フレーム指定の場合
    if input_file_bean.get_frame_specification_flag():
        
        # === 複合チェック ===
        # ビデオストリームがない場合、フレーム指定不可
        if video_stream_bean is None:
            raise Exception('"' + input_file_name + '": video stream is not exists')
        
        # 開始フレームは総フレーム数以下を指定
        if number_utils.is_greater(input_file_bean.get_start_frame(), video_stream_bean.get_nb_frames()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for "start_frame"')
        
        # 切り取りフレーム数（開始フレーム + フレーム数 - 1）は
        # 総フレーム数以下を指定
        trim_frames = input_file_bean.get_start_frame() + input_file_bean.get_frame_number() - 1
        if number_utils.is_greater(trim_frames, video_stream_bean.get_nb_frames()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for trim frames')
        # ====================
        
        start_time = fps_utils.frame_to_sec(input_file_bean.get_start_frame(), video_stream_bean.get_r_frame_rate())
        trim_duration = fps_utils.frame_to_sec(trim_frames, video_stream_bean.get_r_frame_rate())
        start_frame = input_file_bean.get_start_frame()
        
        # フレーム指定でない場合、時間は0以上を指定
    else:
        
        # === 複合チェック ===
        # 開始フレームは動画再生時間以下を指定
        if number_utils.is_greater(input_file_bean.get_start_time(), format_bean.get_duration()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for "start_frame"')
        
        # 終了時間（開始時間 + 切り取り期間）は
        # 動画再生時間以下を指定
        end_time = input_file_bean.get_start_time() + input_file_bean.get_trim_duration()
        if number_utils.is_greater(end_time, format_bean.get_duration()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for trim frames')
        # ====================
        
        start_time = input_file_bean.get_start_time()
        trim_duration = input_file_bean.get_trim_duration()
        start_frame = fps_utils.sec_to_frame(input_file_bean.get_start_time(), video_stream_bean.get_r_frame_rate())
        
    
    # 開始時間指定
    command_input_bean.set_start_time(start_time)
    # 切り取り期間指定
    command_input_bean.set_trim_duration(trim_duration)
    # 開始フレーム指定
    command_input_bean.set_start_frame(start_frame)
    
    # フィルター設定
    
    return command_input_bean
    

