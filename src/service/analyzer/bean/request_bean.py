# ==================================================
# 動画解析リクエストBean
# ==================================================

# ==================================================
# 動画解析リクエストBean
# ==================================================
class AnalyzerRequestBean:
    
    def __init__(self):
        self.__input_file_name = ''
        
    
    # 入力ファイル名
    @property
    def input_file_name(self):
        return self.__input_file_name
    @input_file_name.setter
    def input_file_name(self, input_file_name):
        self.__input_file_name = input_file_name

