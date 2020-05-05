# ==================================================
# 辞書型のリクエストから動画変換リクエストBeanの解析
# ==================================================

from service.marger.bean.request_bean import MargerInputFileBean, MargerOutputFileBean, MargerRequestBean

# 辞書型のリクエストを解析してリクエストBeanを返却
def parse_to_request_bean(request_dict):
    
    # 動画変換入力ファイルBean に格納
    input_bean_list = []
    for input_dict in request_dict['input_file_bean']:
        input_bean_list.append(parse_to_input_bean(input_dict))
    
    # 動画変換出力ファイルBean に格納
    output_dict = request_dict['output_file_bean']
    output_bean = parse_to_output_bean(output_dict)
    
    # 動画変換リクエストBean に格納
    request_bean = MargerRequestBean()
    request_bean.input_file_bean_list = input_bean_list
    request_bean.output_file_bean = output_bean
    
    # 動画変換リクエストBean を返却
    return request_bean

# 動画変換入力ファイルBeanを返却
def parse_to_input_bean(input_file_dict):
    
    input_file_bean = MargerInputFileBean()
    input_file_bean.input_file_name = input_file_dict['input_file_name']
    input_file_bean.start_time = input_file_dict['start_time']
    input_file_bean.trim_duration = input_file_dict['trim_duration']
    input_file_bean.start_frame = input_file_dict['start_frame']
    input_file_bean.end_frame = input_file_dict['end_frame']
    input_file_bean.frame_specification_flag = input_file_dict['frame_specification_flag']
    input_file_bean.video_fade_in_duration = input_file_dict['video_fade_in_duration']
    input_file_bean.video_fade_out_duration = input_file_dict['video_fade_out_duration']
    input_file_bean.audio_fade_in_duration = input_file_dict['audio_fade_in_duration']
    input_file_bean.audio_fade_out_duration = input_file_dict['audio_fade_out_duration']
    
    return input_file_bean

# 動画変換出力ファイルBeanを返却
def parse_to_output_bean(output_file_dict):
    
    output_file_bean = MargerOutputFileBean()
    output_file_bean.overwriting_flag = output_file_dict['overwriting_flag']
    output_file_bean.output_file_name = output_file_dict['output_file_name']
    output_file_bean.codec_type_combination = output_file_dict['codec_type_combination']
    
    return output_file_bean

