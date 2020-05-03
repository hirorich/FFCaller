# ==================================================
# 動画変換レスポンスBean
# ==================================================

# ==================================================
# 動画変換レスポンスBean
# ==================================================
class ResponseBean:
    
    def __init__(self):
        self.__output_file_name = ''
        
    
    # 出力ファイル名
    def get_output_file_name(self):
        return self.__output_file_name
    def set_output_file_name(self, output_file_name):
        self.__output_file_name = output_file_name
    
    # 辞書型に変換
    def parse_to_dict(self):
        bean_dict = dict()
        bean_dict['output_file_name'] = self.__output_file_name
        
        return bean_dict

