# ==================================================
# フレーム分割レスポンスBean
# ==================================================

# ==================================================
# フレーム分割レスポンスBean
# ==================================================
class SegmenterResponseBean:
    
    def __init__(self):
        self.__output_directry_name = ''
        
    
    # 出力フォルダ名
    @property
    def output_directry_name(self):
        return self.__output_directry_name
    @output_directry_name.setter
    def output_directry_name(self, output_directry_name):
        self.__output_directry_name = output_directry_name
    
    # 辞書型に変換
    def parse_to_dict(self):
        bean_dict = dict()
        bean_dict['output_directry_name'] = self.__output_directry_name
        
        return bean_dict

