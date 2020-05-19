# ==================================================
# 設定値
# ==================================================

class _Property:
    
    # 初期値設定
    def __init__(self):
        self.__property_file = ''
        self.__port = 9090
        self.__browser = 'chrome'
        self.__outdir = './_output/'
    
    # 設定ファイル
    @property
    def property_file(self):
        return self.__property_file
    @property_file.setter
    def property_file(self, property_file):
        self.__property_file = property_file
    
    # ポート番号
    @property
    def port(self):
        return self.__port
    @port.setter
    def port(self, port):
        self.__port = port
    
    # ブラウザ
    @property
    def browser(self):
        return self.__browser
    @browser.setter
    def browser(self, browser):
        self.__browser = browser
    
    # 出力先フォルダ
    @property
    def outdir(self):
        return self.__outdir
    @outdir.setter
    def outdir(self, outdir):
        self.__outdir = outdir
    
    # 設定ファイル読み込み
    def read_property_file(self):
        pass

import sys
sys.modules[__name__] = _Property()
