# ==================================================
# ffmpegを用いた動画結合コマンド生成
# ==================================================

from common import app_property

# コマンド生成
def create(output_bean):
    
    # 入力情報整理
    index = 0
    input_list = []
    filter = []
    concat_id = []
    trim_duration = 0
    for input_bean in output_bean.get_input_bean_list():
        input_list.extend(input_bean.create_input_list())
        trim_duration += input_bean.trim_duration()
        if output_bean.with_video:
            video_filter, video_id = input_bean.create_video_filter_list(index)
            filter.extend(video_filter)
            concat_id.append(video_id)
        if output_bean.with_audio:
            audio_filter, audio_id = input_bean.create_audio_filter_list(index)
            filter.extend(audio_filter)
            concat_id.append(audio_id)
        index += 1
    
    # フィルタ情報設定
    concat = []
    concat.append(''.join(concat_id) + 'concat=n=' + str(index))
    if output_bean.with_video:
        concat.append('v=1')
    else:
        concat.append('v=0')
    if output_bean.with_audio:
        concat.append('a=1')
    else:
        concat.append('a=0')
    filter.append(':'.join(concat))
    
    # コマンド設定
    command = [app_property.external_cmd.ffmpeg, '-y', '-v', 'quiet', '-progress', '-']
    command.extend(input_list)
    command.append('-filter_complex')
    command.append(';'.join(filter))
    command.append(output_bean.filepath)
    
    return command, trim_duration
