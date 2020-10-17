# ==================================================
# 環境系定数
# ==================================================

import pathlib
from common import app_property
from common.utility import path_utils

class _Const:
    class ConstError(TypeError):
        pass
    
    WORK_DIR = pathlib.Path(path_utils.convert_to_absolute_path(app_property.eel.init)).joinpath(app_property.workdir)
    DB_FILENAME = path_utils.convert_to_absolute_path(app_property.add_data.ffc_db_sqlite3)
    
    # 新規定数の追加・変更を禁止
    def __setattr__(self, name, value):
        raise self.ConstError('定数の追加・変更はできません (%s)' % name)

import sys
sys.modules[__name__] = _Const()
