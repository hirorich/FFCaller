# ==================================================
# 設定ファイル（jsonファイル）読み込み
# ==================================================

import sys
from common.utility import json_utils, path_utils

# 読み込まれた設定内容
class _Property():
    
    # 設定ファイル読み込み
    def __init__(self, property_file):
        try:
            for k, v in json_utils.json_file_to_object(property_file).__dict__.items():
                self.__setattr__(k, v)
        except:
            pass
    
    # 属性参照
    def __getattr__(self, name):
        if len(self.__dict__) == 0:
            raise ImportError('設定ファイルの読み込み失敗、または設定ファイルが空')
        return self.__dict__[name]
    
    # 属性設定
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('属性の上書きはできません（' + name + '）')
        self.__dict__[name] = value

# モジュールをオブジェクトで上書き
sys.modules[__name__] = _Property(path_utils.convert_to_absolute_path('./env/property.json'))
