# ==================================================
# ����ϊ��̃R���g���[�����i
# ==================================================

from service.converter import convert_command_creater
from service.converter.bean.converter_response_bean import ConverterResponseBean
from service.common import command_runner
from service.common import json_utils

# �ϊ����s
def convert(request_bean):
    
    # �R�}���h�쐬
    command = convert_command_creater.create_command(request_bean)
    
    # ���s
    # proc_stdout = command_runner.run(command, True)
    
    # ����ϊ����X�|���XBean�փZ�b�g
    response_bean = ConverterResponseBean()
    response_bean.set_output_file_name('output.mp4')
    return response_bean
    

