# ==================================================
# json文字列から動画変換リクエストBeanの解析
# ==================================================

from service.marger.bean.request_bean import InputFileBean, OutputFileBean, RequestBean

# リクエストjson文字列を解析してリクエストBeanを返却
def parse_to_request_bean(request_dict):
    
    # 動画変換入力ファイルBean に格納
    input_bean_list = []
    for input_dict in request_dict['input_file_bean']:
        input_bean_list.append(parse_to_input_bean(input_dict))
    
    # 動画変換出力ファイルBean に格納
    output_dict = request_dict['output_file_bean']
    output_bean = parse_to_output_bean(output_dict)
    
    # 動画変換リクエストBean に格納
    request_bean = RequestBean()
    request_bean.set_input_file_bean_list(input_bean_list)
    request_bean.set_output_file_bean(output_bean)
    
    # 動画変換リクエストBean を返却
    return request_bean
    

# 動画変換入力ファイルBeanを返却
def parse_to_input_bean(input_file_dict):
    
    input_file_bean = InputFileBean()
    input_file_bean.set_input_file_name(input_file_dict['input_file_name'])
    input_file_bean.set_start_time(float(input_file_dict['start_time']))
    input_file_bean.set_trim_duration(float(input_file_dict['trim_duration']))
    input_file_bean.set_start_frame(int(input_file_dict['start_frame']))
    input_file_bean.set_frame_number(int(input_file_dict['frame_number']))
    input_file_bean.set_frame_specification_flag(input_file_dict['frame_specification_flag'])
    input_file_bean.set_video_fade_in_duration(float(input_file_dict['video_fade_in_duration']))
    input_file_bean.set_video_fade_out_duration(float(input_file_dict['video_fade_out_duration']))
    input_file_bean.set_audio_fade_in_duration(float(input_file_dict['audio_fade_in_duration']))
    input_file_bean.set_audio_fade_out_duration(float(input_file_dict['audio_fade_out_duration']))
    
    return input_file_bean
    

# 動画変換出力ファイルBeanを返却
def parse_to_output_bean(output_file_dict):
    
    output_file_bean = OutputFileBean()
    output_file_bean.set_overwriting_flag(output_file_dict['overwriting_flag'])
    output_file_bean.set_output_file_name(output_file_dict['output_file_name'])
    output_file_bean.set_codec_type_combination(output_file_dict['codec_type_combination'])
    
    return output_file_bean
    

