# ==================================================
# ffmpegの入力部分設定
# ==================================================

from common.utility import file_utils
from common.utility.type import number_utils, str_utils
from service.analyzer import analyzer_controller
from service.analyzer.bean.request_bean import AnalyzerRequestBean
from service.common import fps_utils
from service.common.ffmpeg.bean.input_bean import FFmpegInputBean

# ffmpegの入力部分設定
def create_input_bean(input_file_bean):
    
    command_input_bean = FFmpegInputBean()
    
    # === 入力チェック ===
    # 入力ファイル名が空白
    input_file_name = input_file_bean.get_input_file_name()
    if str_utils.is_none_or_whitespace(input_file_name):
        raise Exception('"input_file" is not specified')
    
    # 入力ファイルが存在しない
    input_file_name = input_file_name.strip()
    if not file_utils.is_exists(input_file_name):
        raise Exception('"' + input_file_name + '" is not exists')
    
    # 入力ファイル名指定
    command_input_bean.set_input_file_name(input_file_name)
    
    
    
    # 動画情報取得
    analyzer_request_bean = AnalyzerRequestBean()
    analyzer_request_bean.set_input_file_name(input_file_name)
    analyzer_response_bean = analyzer_controller.analize(analyzer_request_bean)
    video_stream_bean = analyzer_response_bean.get_video_stream_bean()
    audio_stream_bean_list = analyzer_response_bean.get_audio_stream_bean_list()
    format_bean = analyzer_response_bean.get_format_bean()
    
    
    
    # フレーム指定の場合
    if input_file_bean.get_frame_specification_flag():
        
        # 開始フレームは1以上を指定
        if number_utils.is_less(input_file_bean.get_start_frame(), 1):
            raise Exception('"' + input_file_name + '": specify at least 1 for "start_frame"')
        
        # フレーム数は1以上を指定
        if number_utils.is_less(input_file_bean.get_end_frame(), 1):
            raise Exception('"' + input_file_name + '": specify at least 1 for "end_frame"')
        
        # === 複合チェック ===
        # ビデオストリームがない場合、フレーム指定不可
        if video_stream_bean is None:
            raise Exception('"' + input_file_name + '": video stream is not exists')
        
        # 開始フレームは総フレーム数以下を指定
        if number_utils.is_greater(input_file_bean.get_start_frame(), video_stream_bean.get_nb_frames()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for "start_frame"')
        
        # 終了フレームは総フレーム数以下を指定
        if number_utils.is_greater(input_file_bean.get_end_frame(), video_stream_bean.get_nb_frames()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for "end_frame"')
        
        # 終了フレームは開始フレーム以上を指定
        if number_utils.is_less(input_file_bean.get_end_frame(), input_file_bean.get_start_frame()):
            raise Exception('"' + input_file_name + '": specify at least ' + str(input_file_bean.get_start_frame()) + ' for "end_frame"')
        
        # 切り取りフレーム数（終了フレーム - 開始フレーム + 1）
        trim_frames = input_file_bean.get_end_frame() - input_file_bean.get_start_frame() + 1
        # ====================
        
        start_time = fps_utils.frame_to_sec(input_file_bean.get_start_frame(), video_stream_bean.get_r_frame_rate())
        trim_duration = fps_utils.frame_to_sec(trim_frames + 1, video_stream_bean.get_r_frame_rate())
        start_frame = input_file_bean.get_start_frame()
        
        
        # フレーム指定でない場合
    else:
        
        # 開始時間は0以上を指定
        if number_utils.is_less(input_file_bean.get_start_time(), 0):
            raise Exception('"' + input_file_name + '": specify at least 0 for "start_time"')
        
        # 切り取り期間は0以上を指定
        if number_utils.is_less(input_file_bean.get_trim_duration(), 0):
            raise Exception('"' + input_file_name + '": specify at least 0 for "trim_duration"')
        
        # === 複合チェック ===
        # 開始フレームは動画再生時間以下を指定
        if number_utils.is_greater(input_file_bean.get_start_time(), format_bean.get_duration()):
            raise Exception('"' + input_file_name + '": specify less than ' + format_bean.get_duration() + ' for "start_frame"')
        
        # 終了時間（開始時間 + 切り取り期間）は
        # 動画再生時間以下を指定
        end_time = input_file_bean.get_start_time() + input_file_bean.get_trim_duration()
        if number_utils.is_greater(end_time, format_bean.get_duration()):
            raise Exception('"' + input_file_name + '": specify less than ' + format_bean.get_duration() + ' for trim frames')
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
    
    
    # ffmpegの入力部分と動画解析結果を返却
    return command_input_bean, analyzer_response_bean

