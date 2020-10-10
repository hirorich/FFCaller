# ==================================================
# ユーザ情報
# ==================================================

import getpass, platform

class _UserInfo:
    
    # システム日付設定
    def __init__(self):
        self.__user_name = getpass.getuser()
        self.__cp_name = platform.uname()[1]
    
    # ユーザ名
    @property
    def user_name(self):
        return self.__user_name
    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name
    
    # PC名
    @property
    def cp_name(self):
        return self.__cp_name
    @cp_name.setter
    def cp_name(self, cp_name):
        self.__cp_name = cp_name

import sys
sys.modules[__name__] = _UserInfo()
