# ==================================================
# json共通部品
# ==================================================

import json

class __Element:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('属性の上書きはできません（' + name + '）')
        self.__dict__[name] = value

# jsonファイルをオブジェクトに変換
def __dict_to_object(obj):
    
    if isinstance(obj, dict):
        obj_dict = __Element()
        for k, v in obj.items():
            obj_dict.__setattr__(k, __dict_to_object(v))
        return obj_dict
    elif isinstance(obj, list) or isinstance(obj, tuple):
        obj_list = []
        for item in obj:
            obj_list.append(__dict_to_object(item))
        return tuple(obj_list)
    else:
        return obj

# jsonファイルをオブジェクトに変換
def json_file_to_object(json_file):
    
    # jsonファイルを読み込む
    with open(json_file) as f:
        dict_json = json.load(f)
    
    # オブジェクトに変換
    return __dict_to_object(dict_json)
