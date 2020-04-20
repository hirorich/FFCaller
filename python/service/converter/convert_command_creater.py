# ==================================================
# ffmpeg��p��������ϊ��R�}���h����
# ==================================================

from service.analyzer import analyzer_controller
from service.analyzer.bean.analyzer_request_bean import AnalyzerRequestBean
from service.converter.bean.command_bean import CommandInputBean
from service.common import file_utils
from service.common import fps_utils
from service.common.type import number_utils
from service.common.type import str_utils

# 
def create_command(request_bean):
    
    # === ���̓`�F�b�N ===
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
        
        input_bean = create_input_bean(input_file_bean)
        print(input_bean.get_input_file_name())
        print(input_bean.get_start_time())
        print(input_bean.get_trim_duration())
        print(input_bean.get_start_frame())
        print(input_bean.create_input_command())
    
    output_file_bean = request_bean.get_output_file_bean()
    print(output_file_bean.get_convert_mode())
    print(output_file_bean.get_overwriting_flag())
    print(output_file_bean.get_output_file_name())
    print(output_file_bean.get_codec_type_combination())
    
    return command
    

def create_input_bean(input_file_bean):
    
    command_input_bean = CommandInputBean()
    
    # === ���̓`�F�b�N ===
    # ���̓t�@�C��������
    input_file_name = input_file_bean.get_input_file_name()
    if str_utils.is_none_or_whitespace(input_file_name):
        raise Exception('"input_file" is not specified')
    
    # ���̓t�@�C�������݂��Ȃ�
    input_file_name = input_file_name.strip()
    if not file_utils.is_exists(input_file_name):
        raise Exception('"' + input_file_name + '" is not exists')
    
    # �t���[���w��̏ꍇ�A�t���[����1�ȏ���w��
    if input_file_bean.get_frame_specification_flag():
        if number_utils.is_less(input_file_bean.get_start_frame(), 1):
            raise Exception('"' + input_file_name + '": specify at least 1 for "start_frame"')
        
        if number_utils.is_less(input_file_bean.get_frame_number(), 1):
            raise Exception('"' + input_file_name + '": specify at least 1 for "frame_number"')
        
        # �t���[���w��łȂ��ꍇ�A���Ԃ�0�ȏ���w��
    else:
        if number_utils.is_less(input_file_bean.get_start_time(), 0):
            raise Exception('"' + input_file_name + '": specify at least 0 for "start_time"')
        
        if number_utils.is_less(input_file_bean.get_trim_duration(), 0):
            raise Exception('"' + input_file_name + '": specify at least 0 for "trim_duration"')
    # ====================
    
    # ���̓t�@�C�����w��
    command_input_bean.set_input_file_name(input_file_name)
    
    # ������擾
    analyzer_request_bean = AnalyzerRequestBean()
    analyzer_request_bean.set_input_file_name(input_file_name)
    analyzer_response_bean = analyzer_controller.analize(analyzer_request_bean)
    format_bean = analyzer_response_bean.get_format_bean()
    video_stream_bean = analyzer_response_bean.get_video_stream_bean()
    audio_stream_bean_list = analyzer_response_bean.get_audio_stream_bean_list()
    print(video_stream_bean.get_r_frame_rate())
    
    # �t���[���w��̏ꍇ
    if input_file_bean.get_frame_specification_flag():
        
        # === �����`�F�b�N ===
        # �r�f�I�X�g���[�����Ȃ��ꍇ�A�t���[���w��s��
        if video_stream_bean is None:
            raise Exception('"' + input_file_name + '": video stream is not exists')
        
        # �J�n�t���[���͑��t���[�����ȉ����w��
        if number_utils.is_greater(input_file_bean.get_start_frame(), video_stream_bean.get_nb_frames()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for "start_frame"')
        
        # �؂���t���[�����i�J�n�t���[�� + �t���[���� - 1�j��
        # ���t���[�����ȉ����w��
        trim_frames = input_file_bean.get_start_frame() + input_file_bean.get_frame_number() - 1
        if number_utils.is_greater(trim_frames, video_stream_bean.get_nb_frames()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for trim frames')
        # ====================
        
        start_time = fps_utils.frame_to_sec(input_file_bean.get_start_frame(), video_stream_bean.get_r_frame_rate())
        trim_duration = fps_utils.frame_to_sec(trim_frames, video_stream_bean.get_r_frame_rate())
        start_frame = input_file_bean.get_start_frame()
        
        # �t���[���w��łȂ��ꍇ�A���Ԃ�0�ȏ���w��
    else:
        
        # === �����`�F�b�N ===
        # �J�n�t���[���͓���Đ����Ԉȉ����w��
        if number_utils.is_greater(input_file_bean.get_start_time(), format_bean.get_duration()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for "start_frame"')
        
        # �I�����ԁi�J�n���� + �؂�����ԁj��
        # ����Đ����Ԉȉ����w��
        end_time = input_file_bean.get_start_time() + input_file_bean.get_trim_duration()
        if number_utils.is_greater(end_time, format_bean.get_duration()):
            raise Exception('"' + input_file_name + '": specify less than ' + video_stream_bean.get_nb_frames() + ' for trim frames')
        # ====================
        
        start_time = input_file_bean.get_start_time()
        trim_duration = input_file_bean.get_trim_duration()
        start_frame = fps_utils.sec_to_frame(input_file_bean.get_start_time(), video_stream_bean.get_r_frame_rate())
        
    
    # �J�n���Ԏw��
    command_input_bean.set_start_time(start_time)
    # �؂�����Ԏw��
    command_input_bean.set_trim_duration(trim_duration)
    # �J�n�t���[���w��
    command_input_bean.set_start_frame(start_frame)
    
    # �t�B���^�[�ݒ�
    
    return command_input_bean
    

