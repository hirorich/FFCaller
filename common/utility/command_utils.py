# ==================================================
# 外部コマンド実行
# ==================================================

# 外部コマンド実行用
import subprocess

# 外部コマンドを実行し、標準出力をリスト形式で返却
def run(cmd, strip_flg=False):
    stdout = []
    proc = subprocess.Popen(args=cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
    for line in proc.stdout:
        try:
            if strip_flg:
                stdout.append(line.decode("UTF-8").strip())
            else:
                stdout.append(line.decode("UTF-8").rstrip())
            
        except:
            continue
    
    return stdout

