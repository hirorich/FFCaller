# ==================================================
# 動画解析のコントロール部品
# ==================================================

from service.analyzer import analyze_command_creater
from service.analyzer.bean.analyzer_response_bean import AnalyzerResponseBean
from service.analyzer.bean.analyzer_response_bean import AnalyzerVideoStreamBean
from service.analyzer.bean.analyzer_response_bean import AnalyzerAudioStreamBean
from service.analyzer.bean.analyzer_response_bean import AnalyzerFormatBean
from service.common import command_runner
from service.common import json_utils

# 解析実行
def analize(request_bean):
    
    # コマンド作成
    command = analyze_command_creater.create_command(request_bean)
    
    # 実行
    proc_stdout = command_runner.run(command, True)
    
    # json文字列から辞書型に変換
    decodeed_video_info = json_utils.decode(''.join(proc_stdout))
    
    # 動画解析レスポンスBeanへセット
    return create_response_bean(decodeed_video_info)
    

# 解析結果から動画解析レスポンスBeanを作成
def create_response_bean(decodeed_video_info):
    
    video_stream_bean = None
    audio_stream_bean_list = []
    format_bean = None
    
    # ストリームのコーデックタイプごとにBeanを作成
    for i in range(len(decodeed_video_info['streams'])):
        codec_type = decodeed_video_info['streams'][i]['codec_type']
        
        # コーデックタイプがvideoの場合、ビデオストリームBeanを作成
        if codec_type == 'video':
            video_stream_bean = create_video_stream_bean(decodeed_video_info['streams'][i])
            
        # コーデックタイプがaudioの場合、オーディオストリームBeanを作成
        elif codec_type == 'audio':
            audio_stream_bean = create_audio_stream_bean(decodeed_video_info['streams'][i])
            audio_stream_bean_list.append(audio_stream_bean)
    
    # フォーマットBeanを作成
    format_bean = create_format_bean(decodeed_video_info['format'])
    
    # 作成したBeanを動画解析レスポンスBeanに設定
    response_bean = AnalyzerResponseBean()
    response_bean.set_video_stream_bean(video_stream_bean)
    response_bean.set_audio_stream_bean_list(audio_stream_bean_list)
    response_bean.set_format_bean(format_bean)
    
    # 動画解析レスポンスBeanを返却
    return response_bean
    

# 解析結果から動画解析ビデオストリームBeanを作成
def create_video_stream_bean(decodeed_stream_info):
    
    video_stream_bean = AnalyzerVideoStreamBean()
    video_stream_bean.set_index(decodeed_stream_info['index'])
    video_stream_bean.set_codec_type(decodeed_stream_info['codec_type'])
    video_stream_bean.set_codec_name(decodeed_stream_info['codec_name'])
    video_stream_bean.set_codec_long_name(decodeed_stream_info['codec_long_name'])
    video_stream_bean.set_duration(decodeed_stream_info['duration'])
    video_stream_bean.set_bit_rate(decodeed_stream_info['bit_rate'])
    video_stream_bean.set_width(decodeed_stream_info['width'])
    video_stream_bean.set_height(decodeed_stream_info['height'])
    video_stream_bean.set_r_frame_rate(decodeed_stream_info['r_frame_rate'])
    video_stream_bean.set_nb_frames(decodeed_stream_info['nb_frames'])
    
    return video_stream_bean
    

# 解析結果から動画解析オーディオストリームBeanを作成
def create_audio_stream_bean(decodeed_stream_info):
    
    audio_stream_bean = AnalyzerAudioStreamBean()
    audio_stream_bean.set_index(decodeed_stream_info['index'])
    audio_stream_bean.set_codec_type(decodeed_stream_info['codec_type'])
    audio_stream_bean.set_codec_name(decodeed_stream_info['codec_name'])
    audio_stream_bean.set_codec_long_name(decodeed_stream_info['codec_long_name'])
    audio_stream_bean.set_duration(decodeed_stream_info['duration'])
    audio_stream_bean.set_bit_rate(decodeed_stream_info['bit_rate'])
    audio_stream_bean.set_sample_rate(decodeed_stream_info['sample_rate'])
    
    return audio_stream_bean
    

# 解析結果から動画解析フォーマットBeanを作成
def create_format_bean(decodeed_stream_info):
    
    format_bean = AnalyzerFormatBean()
    format_bean.set_filename(decodeed_stream_info['filename'])
    format_bean.set_nb_streams(decodeed_stream_info['nb_streams'])
    format_bean.set_duration(decodeed_stream_info['duration'])
    format_bean.set_size(decodeed_stream_info['size'])
    
    return format_bean
    

