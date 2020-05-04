# ==================================================
# フレーム分割のコントロール部品
# ==================================================

from service.segmenter import segmente_command_creater
from service.segmenter.bean.response_bean import SegmenterResponseBean
from service.common import command_runner

# フレーム分割実行
def segment(request_bean):
    
    # コマンド作成
    command = segmente_command_creater.create_command(request_bean)
    
    # 実行
    proc_stdout = command_runner.run(command, True)
    
    # フレーム分割レスポンスBeanへセット
    response_bean = SegmenterResponseBean()
    response_bean.output_file_name = request_bean.output_file_bean.output_file_name
    return response_bean

