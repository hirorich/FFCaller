# ==================================================
# ffprobe��p���������̓R�}���h����
# ==================================================

from service.common.type import str_utils
from service.common import file_utils

# �R�}���h����
def create_command(request_bean):
    
    # === ���̓`�F�b�N ===
    # ���̓t�@�C��������
    input = request_bean.get_input_file_name()
    if str_utils.is_none_or_whitespace(input):
        raise Exception('input_file is not specified')
    
    # ���̓t�@�C�������݂��Ȃ�
    input = input.strip()
    if not file_utils.is_exists(input):
        raise Exception(input + ' is not exists')
    # ====================
    
    # �R�}���h����
    command = [r'ffprobe', r'-v', r'quiet', r'-show_format', r'-show_streams', r'-print_format', r'json']
    command.append(input)
    
    return command

