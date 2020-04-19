# ==================================================
# json文字列から動画変換リクエストBeanの解析
# ==================================================

from service.converter.bean.converter_request_bean import ConverterInputFileBean
from service.converter.bean.converter_request_bean import ConverterOutputFileBean
from service.converter.bean.converter_request_bean import ConverterRequestBean
from service.converter.enum import MultimediaTypeEnum
from service.converter.enum import ConverterModeEnum

# リクエストjson文字列を解析してリクエストBeanを返却
def parse_to_request_bean(request_json_string):
    
    # ====== スタブ ======
    request_bean = stub_request_bean()
    return request_bean
    # ====================
    
    # ===== 実装予定 =====
    # json形式の文字列をdict型に変換
    # 動画変換入力ファイルBean に格納
    # 動画変換出力ファイルBean に格納
    # 動画変換リクエストBean に格納
    # ====================
    
    # 動画変換リクエストBean を返却
    return request_bean
    

# スタブ用のリクエストBeanを返却
def stub_request_bean():
    
    # ====== スタブ ======
    input_file_bean = ConverterInputFileBean()
    input_file_bean.set_input_file_name(r'../input2.mp4')
    input_file_bean.set_start_time(2.1666)
    input_file_bean.set_trim_duration(5.25)
    input_file_bean.set_start_frame(1)
    input_file_bean.set_frame_number(100)
    input_file_bean.set_frame_specification_flag(False)
    input_file_bean.set_video_fade_in_duration(1)
    input_file_bean.set_video_fade_out_duration(1)
    input_file_bean.set_audio_fade_in_duration(1)
    input_file_bean.set_audio_fade_out_duration(1)
    input_file_bean_list = []
    input_file_bean_list.append(input_file_bean)
    
    output_file_bean = ConverterOutputFileBean()
    output_file_bean.set_convert_mode(ConverterModeEnum.TRIM)
    output_file_bean.set_overwriting_flag(True)
    output_file_bean.set_output_file_name(r'./_output/video/output.mp4')
    output_file_bean.set_codec_type_combination(MultimediaTypeEnum.VIDEO_AND_AUDIO)
    
    request_bean = ConverterRequestBean()
    request_bean.set_input_file_bean_list(input_file_bean_list)
    request_bean.set_output_file_bean(output_file_bean)
    # ====================
    
    # 動画変換リクエストBean を返却
    return request_bean
    

