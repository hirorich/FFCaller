# 起動引数使用のため
import argparse

# ファイル情報の取得
from service import multimedia_analyzer
from service import multimedia_converter

# main
if __name__ == "__main__":
    
    # 動画解析処理実行
    # result = multimedia_analyzer.exec('{"service_request":{"input_file_name":"../../input2.mp4"}}')
    # print(result)
    
    # 動画変換処理実行
    result = multimedia_converter.exec('{"service_request":{"input_file_bean":[{"input_file_name":"../../input2.mp4","start_time":2.1666,"trim_duration":5.25,"start_frame":11,"frame_number":100,"frame_specification_flag":false,"video_fade_in_duration":1,"video_fade_out_duration":2,"audio_fade_in_duration":1,"audio_fade_out_duration":2}],"output_file_bean":{"convert_mode":1,"overwriting_flag":true,"output_file_name":"./_output/video/output.mp4","codec_type_combination":1}}}')
    # result = multimedia_converter.exec('{"service_request":{"input_file_bean":[{"input_file_name":"../../input2.mp4","start_time":2.1666,"trim_duration":5.25,"start_frame":11,"frame_number":100,"frame_specification_flag":false,"video_fade_in_duration":1,"video_fade_out_duration":2,"audio_fade_in_duration":1,"audio_fade_out_duration":2}],"output_file_bean":{"convert_mode":2,"overwriting_flag":true,"output_file_name":"./_output/frame/output.mp4","codec_type_combination":1}}}')
    print(result)
    

