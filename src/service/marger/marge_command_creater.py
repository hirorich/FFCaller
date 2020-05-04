# ==================================================
# ffmpegを用いた動画変換コマンド生成
# ==================================================

import os
from service.common.ffmpeg import ffmpeg_input_creater
from common.utility.type import number_utils, str_utils

# コマンド作成
def create_command(request_bean):
    
    input_file_bean_list = request_bean.get_input_file_bean_list()
    input_bean_list = []
    for i in range(len(input_file_bean_list)):
        input_file_bean = input_file_bean_list[i]
        
        input_bean = create_input_bean(input_file_bean, i)
        input_bean_list.append(input_bean)
    
    output_file_bean = request_bean.get_output_file_bean()
    
    command = marge_command(input_bean_list, output_file_bean)
    print(command)
    return command

# コマンドの入力部分作成
def create_input_bean(input_file_bean, file_index):
    
    # コマンドの入力部分と解析情報取得
    command_input_tuple = ffmpeg_input_creater.create_input_bean(input_file_bean)
    command_input_bean = command_input_tuple[0]
    analyzer_response_bean = command_input_tuple[1]
    
    input_file_name = command_input_bean.get_input_file_name()
    trim_duration = command_input_bean.get_trim_duration()
    format_bean = analyzer_response_bean.get_format_bean()
    video_stream_bean = analyzer_response_bean.get_video_stream_bean()
    audio_stream_bean_list = analyzer_response_bean.get_audio_stream_bean_list()
    
    
    
    # フィルター設定
    filter_string = ''
    
    # 映像フィルター設定
    if video_stream_bean is not None:
        filtered_count = 0
        stream_index = video_stream_bean.get_index()
        filtered_id = '[' + str(file_index) + ':' + str(stream_index) + ']'
        
        # 映像フェードイン
        fade_in_duration = input_file_bean.get_video_fade_in_duration()
        if fade_in_duration > 0:
            if number_utils.is_greater(fade_in_duration, trim_duration):
                raise Exception('"' + input_file_name + '": specify less than trim_duration for fade_in_duration')
            
            filtered_count += 1
            new_filtered_id = create_filtered_id(file_index, stream_index, filtered_count)
            filter_string += filtered_id + 'fade=t=in:st=0:d=' + str(fade_in_duration) + new_filtered_id + ';'
            filtered_id = new_filtered_id
        
        # 映像フェードアウト
        fade_out_duration = input_file_bean.get_video_fade_out_duration()
        if fade_out_duration > 0:
            if number_utils.is_greater(fade_out_duration, trim_duration):
                raise Exception('"' + input_file_name + '": specify less than trim_duration for fade_out_duration')
            
            filtered_count += 1
            new_filtered_id = create_filtered_id(file_index, stream_index, filtered_count)
            filter_string += filtered_id + 'fade=t=out:st=' + str(trim_duration - fade_out_duration) + ':d=' + str(fade_out_duration) + new_filtered_id + ';'
            filtered_id = new_filtered_id
        
        # 映像識別子指定
        command_input_bean.set_filtered_video_id(filtered_id)
    
    # 音声フィルター設定
    if audio_stream_bean_list is not None:
        if len(audio_stream_bean_list) > 0:
            audio_stream_bean = audio_stream_bean_list[0]
            
            filtered_count = 0
            stream_index = audio_stream_bean.get_index()
            filtered_id = '[' + str(file_index) + ':' + str(stream_index) + ']'
            
            # 音声フェードイン
            fade_in_duration = input_file_bean.get_audio_fade_in_duration()
            if fade_in_duration > 0:
                if number_utils.is_greater(fade_in_duration, trim_duration):
                    raise Exception('"' + input_file_name + '": specify less than trim_duration for fade_in_duration')
                
                filtered_count += 1
                new_filtered_id = create_filtered_id(file_index, stream_index, filtered_count)
                filter_string += filtered_id + 'afade=t=in:st=0:d=' + str(fade_in_duration) + new_filtered_id + ';'
                filtered_id = new_filtered_id
            
            # 音声フェードアウト
            fade_out_duration = input_file_bean.get_audio_fade_out_duration()
            if fade_out_duration > 0:
                if number_utils.is_greater(fade_out_duration, trim_duration):
                    raise Exception('"' + input_file_name + '": specify less than trim_duration for fade_out_duration')
                
                filtered_count += 1
                new_filtered_id = create_filtered_id(file_index, stream_index, filtered_count)
                filter_string += filtered_id + 'afade=t=out:st=' + str(trim_duration - fade_out_duration) + ':d=' + str(fade_out_duration) + new_filtered_id + ';'
                filtered_id = new_filtered_id
            
            # 映像識別子指定
            command_input_bean.set_filtered_audio_id(filtered_id)
    
    # フィルター指定
    command_input_bean.set_filter_string(filter_string)
    
    return command_input_bean

# 映像・音声識別子作成
def create_filtered_id(file_index, stream_index, count):
    return '[f' + str(file_index) + 'i' + str(stream_index) + 'c' + str(count) + ']'

# コマンドの入出力部分を組み合わせる
def marge_command(input_bean_list, output_file_bean):
    
    command = []
    filter = ''
    filter_id = ''
    
    command.append('ffmpeg')
    
    # 上書き可否
    if output_file_bean.get_overwriting_flag():
        command.append('-y')
    
    # 入力部分を組み合わせる
    file_count = 0
    video_count = 0
    audio_count = 0
    for input_bean in input_bean_list:
        
        file_count += 1
        if (number_utils.is_equal(output_file_bean.get_codec_type_combination(), 2)
            or number_utils.is_equal(output_file_bean.get_codec_type_combination(), 1)):
            if not str_utils.is_none_or_empty(input_bean.get_filtered_video_id()):
                video_count += 1
                filter_id += input_bean.get_filtered_video_id()
        if (number_utils.is_equal(output_file_bean.get_codec_type_combination(), 3)
            or number_utils.is_equal(output_file_bean.get_codec_type_combination(), 1)):
            if not str_utils.is_none_or_empty(input_bean.get_filtered_audio_id()):
                audio_count += 1
                filter_id += input_bean.get_filtered_audio_id()
        
        command.extend(input_bean.create_input_command())
        filter += input_bean.get_filter_string()
    
    # フィルタ文字列作成
    filter += filter_id + 'concat=n=' + str(file_count)
    
    if number_utils.is_equal(video_count, 0):
        filter += ':v=0'
    elif number_utils.is_equal(video_count, file_count):
        filter += ':v=1'
    else:
        raise Exception('全て映像なし または 全て映像ありのみ結合可能')
    
    if number_utils.is_equal(audio_count, 0):
        filter += ':a=0'
    elif number_utils.is_equal(audio_count, file_count):
        filter += ':a=1'
    else:
        raise Exception('全て音声なし または 全て音声ありのみ結合可能')
    
    # 出力ファイル名指定
    output_file_name = output_file_bean.get_output_file_name()
    
    # フィルタ指定
    command.append('-filter_complex')
    command.append(filter)
    
    command.append(output_file_name)
    
    return command

