# ==================================================
# フレーム分割リクエストBean
# ==================================================

# ==================================================
# フレーム分割リクエストBean
# ==================================================
class RequestBean:
    
    def __init__(self):
        self.__input_file_bean_list = []
        self.__output_file_bean = None
        
    
    # 入力ファイルBean
    def get_input_file_bean(self):
        return self.__input_file_bean
    def set_input_file_bean(self, input_file_bean):
        self.__input_file_bean = input_file_bean
    
    # 出力ファイルBean
    def get_output_file_bean(self):
        return self.__output_file_bean
    def set_output_file_bean(self, output_file_bean):
        self.__output_file_bean = output_file_bean

# ==================================================
# フレーム分割入力ファイルBean
# ==================================================
class InputFileBean:
    
    def __init__(self):
        self.__input_file_name = ''
        self.__start_time = 0
        self.__trim_duration = 0
        self.__start_frame = 1
        self.__frame_number = 1
        self.__frame_specification_flag = False
    
    # 入力ファイル名
    def get_input_file_name(self):
        return self.__input_file_name
    def set_input_file_name(self, input_file_name):
        self.__input_file_name = input_file_name
    
    # 開始時間
    def get_start_time(self):
        return self.__start_time
    def set_start_time(self, start_time):
        self.__start_time = start_time
    
    # 切り取り期間
    def get_trim_duration(self):
        return self.__trim_duration
    def set_trim_duration(self, trim_duration):
        self.__trim_duration = trim_duration
    
    # 開始フレーム
    def get_start_frame(self):
        return self.__start_frame
    def set_start_frame(self, start_frame):
        self.__start_frame = start_frame
    
    # フレーム数
    def get_frame_number(self):
        return self.__frame_number
    def set_frame_number(self, frame_number):
        self.__frame_number = frame_number
    
    # フレーム指定フラグ
    def get_frame_specification_flag(self):
        return self.__frame_specification_flag
    def set_frame_specification_flag(self, frame_specification_flag):
        self.__frame_specification_flag = frame_specification_flag

# ==================================================
# フレーム分割出力ファイルBean
# ==================================================
class OutputFileBean:
    
    def __init__(self):
        self.__overwriting_flag = True
        self.__output_file_name = ''
        
    
    # 上書きフラグ
    def get_overwriting_flag(self):
        return self.__overwriting_flag
    def set_overwriting_flag(self, overwriting_flag):
        self.__overwriting_flag = overwriting_flag
    
    # 出力ファイル名
    def get_output_file_name(self):
        return self.__output_file_name
    def set_output_file_name(self, output_file_name):
        self.__output_file_name = output_file_name

