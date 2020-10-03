# ==================================================
# eelの呼び出し単位で作成
# 共通・特化できる部分はパッケージに分類して作成
# ==================================================

from common import app_property
from common.utility import log_utils
from service.common import frame_time_converter
from service.ffc.sql import ffc_select
from service.marger import marge_ffmpeg
from service.marger.bean.marger_input_bean import MargerInputBean
from service.marger.bean.marger_output_bean import MargerOutputBean

# 実行
def exec(conn):
    try:
        # マージ実行
        marge_ffmpeg.marge(__create_output_bean(conn))
        
    except Exception as e:
        message = log_utils.write_exception(e)

# 出力ビーン作成
def __create_output_bean(conn):
    output_bean = MargerOutputBean()
    with_video = True
    with_audio = True
    for target in ffc_select.get_targets(conn):
        
        # ターゲット情報取得取得
        trim = ffc_select.get_trim(conn, target.target_id)
        file = ffc_select.get_file(conn, target.file_id)
        video_stream = ffc_select.get_video_stream(conn, target.file_id)
        audio_streams = ffc_select.get_audio_streams(conn, target.file_id)
        
        # 映像・音声有無
        with_video = with_video and (video_stream is not None)
        with_audio = with_audio and (len(audio_streams) > 0)
        
        # 入力ビーン設定
        input_bean = MargerInputBean()
        input_bean.workpath = file.workpath
        if trim.frame_input_flag:
            start_time, end_time = frame_time_converter.frame_to_time(trim.start_frame, trim.end_frame, video_stream.video.r_frame_rate)
            input_bean.start_time = start_time
            input_bean.end_time = end_time
        else:
            input_bean.start_time = trim.start_time
            input_bean.end_time = trim.end_time
        input_bean.video_fade_in = trim.video_fade_in
        input_bean.video_fade_out = trim.video_fade_out
        input_bean.audio_fade_in = trim.audio_fade_in
        input_bean.audio_fade_out = trim.audio_fade_out
        
        # 出力ビーンに格納
        output_bean.append_input_bean(input_bean)
    
    # 出力ストリーム指定
    output_bean.with_video = with_video
    output_bean.with_audio = with_audio
    
    # 出力ファイル名指定
    if output_bean.with_video:
        output_bean.filepath = r'output.mp4'
    elif output_bean.with_audio:
        output_bean.filepath = r'output.mp3'
    
    return output_bean
