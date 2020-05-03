# ==================================================
# コマンドBean
# ==================================================

# ==================================================
# コマンドインプットBean
# ==================================================
class CommandInputBean:
    
    def __init__(self):
        self.__input_file_name = ''
        self.__start_time = 0
        self.__trim_duration = 0
        
        self.__start_frame = 1
        
    
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
    
    
    
    # 
    def create_input_command(self):
        command = []
        command.append("-ss")
        command.append(str(self.__start_time))
        command.append("-t")
        command.append(str(self.__trim_duration))
        command.append("-i")
        command.append(self.__input_file_name)
        return command
    

