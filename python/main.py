# 起動引数使用のため
import argparse

# ファイル情報の取得
from service import multimedia_analyzer
from service import multimedia_converter

# main
if __name__ == "__main__":
    
    # 動画解析処理実行
    result = multimedia_analyzer.exec('{"service_request":{"input_file_name":"../input2.mp4"}}')
    print(result)
    
    # 動画変換処理実行
    # multimedia_converter.exec('TEST')
    

