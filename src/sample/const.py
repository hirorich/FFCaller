# ==================================================
# 定数
# https://maku77.github.io/python/syntax/const.html
# ==================================================

class _Const:
    class ConstError(TypeError):
        pass
    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _Const()
