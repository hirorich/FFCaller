# ==================================================
# フレーム分割のコントロール部品
# ==================================================

from common.utility import command_utils
from service.segmenter import segmente_command_creater
from service.segmenter.bean.response_bean import SegmenterResponseBean

# フレーム分割実行
def segment(request_bean):
    
    # コマンド作成
    command = segmente_command_creater.create_command(request_bean)
    
    # 実行
    proc_stdout = command_utils.run(command, True)
    
    # フレーム分割レスポンスBeanへセット
    response_bean = SegmenterResponseBean()
    response_bean.output_directry_name = request_bean.output_file_bean.output_directry_name
    return response_bean

