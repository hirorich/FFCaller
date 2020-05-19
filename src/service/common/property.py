# ==================================================
# 設定値
# ==================================================

class _Property:
    
    # 初期値設定
    def __init__(self):
        self.__property_file = ''
        self.__port = 9090
        self.__browser = 'chrome'
        self.__outdir_marge = './_output'
        self.__outdir_segment = './_output/frame'
    
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
    
    # 動画変換出力先フォルダ
    @property
    def outdir_marge(self):
        return self.__outdir_marge
    @outdir_marge.setter
    def outdir_marge(self, outdir_marge):
        self.__outdir_marge = outdir_marge
    
    # フレーム分割出力先フォルダ
    @property
    def outdir_segment(self):
        return self.__outdir_segment
    @outdir_segment.setter
    def outdir_segment(self, outdir_segment):
        self.__outdir_segment = outdir_segment
    
    # 設定ファイル読み込み
    def read_property_file(self):
        pass

import sys
sys.modules[__name__] = _Property()
