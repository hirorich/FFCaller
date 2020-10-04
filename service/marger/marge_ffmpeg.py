# ==================================================
# マージ実行
# ==================================================

import subprocess
from datetime import datetime, timedelta
from common.error import error_id
from common.error.business_error import BusinessError
from common.utility import file_utils, log_utils
from service.marger import command_creater

# 実行
def marge(output_bean):
    
    # コマンド作成
    command, trim_duration = command_creater.create(output_bean)
    
    # 実行
    __run(command, trim_duration)
    
    # 出力ファイルチェック
    if not file_utils.is_exists(output_bean.filepath):
        raise BusinessError(error_id.E0000002, output_bean.filepath)

# コマンドを実行し、進捗率を算出
def __run(cmd, trim_duration):
    proc = subprocess.Popen(args=cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    for line in proc.stdout:
        try:
            log = line.decode("UTF-8").strip().split('=')
            if len(log) >= 2 and log[0] == 'out_time':
                dt = datetime.strptime(log[1], '%H:%M:%S.%f')
                total_seconds = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second, microseconds=dt.microsecond).total_seconds()
                log_utils.writeline_info(str(total_seconds/trim_duration*100) + '%')
            
        except:
            continue
