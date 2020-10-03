# ==================================================
# マージ実行
# ==================================================

# 実行
def exec(output_bean):
    pass

def __create_command(output_bean):
    index = 0
    for input_bean in output_bean.get_input_bean_list():
        input_list = input_bean.create_input_list()
        filter_list, video_id, audio_id = input_bean.create_filter_list(index)
