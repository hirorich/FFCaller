# ==================================================
# 文字列型(str型)共通部品
# ==================================================

from service.common.type import type_utils

# None、または空文字の場合True
def is_none_or_empty(string):
    
    if type_utils.is_none(string):
        return True
    
    if not type_utils.is_str(string):
        raise TypeError('parameter is not str type')
    
    return (len(string) == 0)
    

# None、または空白の場合True
def is_none_or_whitespace(string):
    
    if type_utils.is_none(string):
        return True
    
    if not type_utils.is_str(string):
        raise TypeError('parameter is not str type')
    
    return (len(string.strip()) == 0)
    

