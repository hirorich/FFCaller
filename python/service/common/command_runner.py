# ==================================================
# 外部コマンド実行
# ==================================================

# 外部コマンド実行用
import subprocess

# 外部コマンドを実行し、標準出力をリスト形式で返却
def run(cmd, strip_flg=False):
    stdout = list()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in proc.stdout:
        try:
            if strip_flg:
                stdout.append(line.decode("UTF-8").strip())
            else:
                stdout.append(line.decode("UTF-8").rstrip())
            
        except:
            continue
        
    
    return stdout

