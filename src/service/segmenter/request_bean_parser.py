# ==================================================
# 辞書型のリクエストからフレーム分割リクエストBeanの解析
# ==================================================

from service.segmenter.bean.request_bean import SegmenterInputFileBean, SegmenterOutputFileBean, SegmenterRequestBean

# 辞書型のリクエストを解析してリクエストBeanを返却
def parse_to_request_bean(request_dict):
    
    # 動画変換入力ファイルBean に格納
    input_dict = request_dict['input_file_bean']
    input_bean = parse_to_input_bean(input_dict)
    
    # 動画変換出力ファイルBean に格納
    output_dict = request_dict['output_file_bean']
    output_bean = parse_to_output_bean(output_dict)
    
    # 動画変換リクエストBean に格納
    request_bean = SegmenterRequestBean()
    request_bean.input_file_bean = input_bean
    request_bean.output_file_bean = output_bean
    
    # 動画変換リクエストBean を返却
    return request_bean

# フレーム分割入力ファイルBeanを返却
def parse_to_input_bean(input_file_dict):
    
    input_file_bean = SegmenterInputFileBean()
    input_file_bean.input_file_name = input_file_dict['input_file_name']
    input_file_bean.start_time = float(input_file_dict['start_time'])
    input_file_bean.trim_duration = float(input_file_dict['trim_duration'])
    input_file_bean.start_frame = int(input_file_dict['start_frame'])
    input_file_bean.end_frame = int(input_file_dict['end_frame'])
    input_file_bean.frame_specification_flag = input_file_dict['frame_specification_flag']
    
    return input_file_bean

# フレーム分割出力ファイルBeanを返却
def parse_to_output_bean(output_file_dict):
    
    output_file_bean = SegmenterOutputFileBean()
    output_file_bean.overwriting_flag = output_file_dict['overwriting_flag']
    output_file_bean.output_file_name = output_file_dict['output_file_name']
    
    return output_file_bean

