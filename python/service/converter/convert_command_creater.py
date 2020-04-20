# ==================================================
# ffmpegを用いた動画変換コマンド生成
# ==================================================

# 
def create_command(request_bean):
    
    # === 入力チェック ===
    # ====================
    
    command = []
    
    for input_file_bean in request_bean.get_input_file_bean_list():
        print(input_file_bean.get_input_file_name())
        print(input_file_bean.get_start_time())
        print(input_file_bean.get_trim_duration())
        print(input_file_bean.get_start_frame())
        print(input_file_bean.get_frame_number())
        print(input_file_bean.get_frame_specification_flag())
        print(input_file_bean.get_video_fade_in_duration())
        print(input_file_bean.get_video_fade_out_duration())
        print(input_file_bean.get_audio_fade_in_duration())
        print(input_file_bean.get_audio_fade_out_duration())
        
    
    output_file_bean = request_bean.get_output_file_bean()
    print(output_file_bean.get_convert_mode())
    print(output_file_bean.get_overwriting_flag())
    print(output_file_bean.get_output_file_name())
    print(output_file_bean.get_codec_type_combination())
    
    return command
    

