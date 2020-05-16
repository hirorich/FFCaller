# ==================================================
# ffmpegの入力部分設定
# ==================================================

from common.error.business_error import BusinessError
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
    input_file_name = input_file_bean.input_file_name
    if str_utils.is_none_or_whitespace(input_file_name):
        raise BusinessError('E0000001')
    
    # 入力ファイルが存在しない
    input_file_name = input_file_name.strip()
    if not file_utils.is_exists(input_file_name):
        raise BusinessError('E0000002', input_file_name)
    
    # 入力ファイル名指定
    command_input_bean.input_file_name = input_file_name
    
    
    
    # 動画情報取得
    analyzer_request_bean = AnalyzerRequestBean()
    analyzer_request_bean.input_file_name = input_file_name
    analyzer_response_bean = analyzer_controller.analize(analyzer_request_bean)
    video_stream_bean = analyzer_response_bean.video_stream_bean
    audio_stream_bean_list = analyzer_response_bean.audio_stream_bean_list
    format_bean = analyzer_response_bean.format_bean
    
    
    
    # フレーム指定の場合
    if input_file_bean.frame_specification_flag:
        
        # 開始フレームは1以上を指定
        if number_utils.is_less(input_file_bean.start_frame, 1):
            raise BusinessError('E0000003', 'start_frame' ,'1' , input_file_name)
        
        # フレーム数は1以上を指定
        if number_utils.is_less(input_file_bean.end_frame, 1):
            raise BusinessError('E0000003', 'end_frame' ,'1' , input_file_name)
        
        # === 複合チェック ===
        # ビデオストリームがない場合、フレーム指定不可
        if video_stream_bean is None:
            raise BusinessError('E0000008', input_file_name)
        
        # 開始フレームは総フレーム数以下を指定
        if number_utils.is_greater(input_file_bean.start_frame, video_stream_bean.nb_frames):
            raise BusinessError('E0000004', 'start_frame', str(video_stream_bean.nb_frames), input_file_name)
        
        # 終了フレームは総フレーム数以下を指定
        if number_utils.is_greater(input_file_bean.end_frame, video_stream_bean.nb_frames):
            raise BusinessError('E0000004', 'end_frame', str(video_stream_bean.nb_frames), input_file_name)
        
        # 終了フレームは開始フレーム以上を指定
        if number_utils.is_less(input_file_bean.end_frame, input_file_bean.start_frame):
            raise BusinessError('E0000003', 'end_frame' ,str(input_file_bean.start_frame) , input_file_name)
        
        # 切り取りフレーム数（終了フレーム - 開始フレーム + 1）
        trim_frames = input_file_bean.end_frame - input_file_bean.start_frame + 1
        # ====================
        
        start_time = fps_utils.frame_to_sec(input_file_bean.start_frame, video_stream_bean.r_frame_rate)
        trim_duration = fps_utils.frame_to_sec(trim_frames + 1, video_stream_bean.r_frame_rate)
        start_frame = input_file_bean.start_frame
        
        
        # フレーム指定でない場合
    else:
        
        # 開始時間は0以上を指定
        if number_utils.is_less(input_file_bean.start_time, 0):
            raise BusinessError('E0000003', 'start_time' ,'0' , input_file_name)
        
        # 切り取り期間は0以上を指定
        if number_utils.is_less(input_file_bean.trim_duration, 0):
            raise BusinessError('E0000003', 'trim_duration' ,'0' , input_file_name)
        
        # === 複合チェック ===
        # 開始フレームは動画再生時間以下を指定
        if number_utils.is_greater(input_file_bean.start_time, format_bean.duration):
            raise BusinessError('E0000004', 'start_frame', str(format_bean.duration), input_file_name)
        
        # 終了時間（開始時間 + 切り取り期間）は
        # 動画再生時間以下を指定
        end_time = input_file_bean.start_time + input_file_bean.trim_duration
        if number_utils.is_greater(end_time, format_bean.duration):
            raise BusinessError('E0000004', 'start_frameとtrim_durationの合計', str(format_bean.duration), input_file_name)
        # ====================
        
        start_time = input_file_bean.start_time
        trim_duration = input_file_bean.trim_duration
        start_frame = fps_utils.sec_to_frame(input_file_bean.start_time, video_stream_bean.r_frame_rate)
        
    
    # 開始時間指定
    command_input_bean.start_time = start_time
    # 切り取り期間指定
    command_input_bean.trim_duration = trim_duration
    # 開始フレーム指定
    command_input_bean.start_frame = start_frame
    
    
    # ffmpegの入力部分と動画解析結果を返却
    return command_input_bean, analyzer_response_bean

