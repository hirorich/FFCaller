# ==================================================
# ffmpegを用いたフレーム分割コマンド生成
# ==================================================

import os
from service.common.ffmpeg import ffmpeg_input_creater

# コマンド作成
def create_command(request_bean):
    
    input_file_bean = request_bean.get_input_file_bean()
    input_bean = create_input_bean(input_file_bean)
    
    output_file_bean = request_bean.get_output_file_bean()
    
    command = marge_command(input_bean, output_file_bean)
    print(command)
    return command

# コマンドの入力部分作成
def create_input_bean(input_file_bean):
    
    command_input_bean = ffmpeg_input_creater.create_input_bean(input_file_bean)
    
    return command_input_bean[0]

# コマンドの入出力部分を組み合わせる
def marge_command(input_bean, output_file_bean):
    
    command = []
    
    command.append('ffmpeg')
    
    # 上書き可否
    if output_file_bean.get_overwriting_flag():
        command.append('-y')
    
    # 入力ファイル名指定
    command.extend(input_bean.create_input_command())
    
    # 切り取り開始フレーム番号
    command.append('-f')
    command.append('image2')
    command.append('-start_number')
    command.append(str(input_bean.get_start_frame()))
    
    # 出力ファイル名指定
    output_file_name = output_file_bean.get_output_file_name()
    file_name = os.path.splitext(os.path.basename(output_file_name))[0]
    file_name += '_%06d.png'
    dir_name = os.path.dirname(output_file_name)
    output_file_name = dir_name + '/' + file_name
    command.append(output_file_name)
    
    return command

