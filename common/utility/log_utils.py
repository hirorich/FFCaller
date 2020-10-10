# ==================================================
# ログ共通部品
# ==================================================

import traceback
from common import system_datetime, user_info
from common.utility import message_utils
from common.error.business_error import BusinessError

class _LogUtil:
    
    # システム日付を基にファイル名指定
    def __init__(self):
        self.__path = './log_' + system_datetime.system_datetime.strftime('%Y%m%d_%H%M%S') + '.md'
    
    # ログファイル出力
    def __write_log(self, message, level):
        try:
            # メッセージ内容修正
            if(len(message) == 0 or message[-1] != '\n'):
                message = message + '\n'
            message = message.replace('~', '～')
            
            # システム処理日付取得
            sys_now = system_datetime.now.strftime('%Y/%m/%d %H:%M:%S.%f')
            
            # ログファイル出力
            with open(self.__path, mode='a', encoding='utf-8') as f:
                f.write('### [' + sys_now + '] [' + level + '] [' + user_info.user_name + '] [' + user_info.cp_name + ']\n')
                f.write('~~~\n')
                f.write(message)
                f.write('~~~\n')
        except:
            pass
    
    # INFOログファイル出力
    def writeline_info(self, message):
        self.__write_log(message, 'INFO')
    
    # WARNINGログファイル出力
    def writeline_warning(self, message):
        self.__write_log(message, 'WARNING')
    
    # ERRORログファイル出力
    def writeline_error(self, message):
        self.__write_log(message, 'ERROR')
    
    # FATALログファイル出力
    def writeline_fatal(self, message):
        self.__write_log(message, 'FATAL')
    
    # 例外出力
    def write_exception(self, e):
        
        # スタックトレースと例外メッセージ出力
        self.writeline_error(traceback.format_exc())
        
        # ビジネスエラーのメッセージを取得
        if isinstance(e, BusinessError):
            message = message_utils.get_business_error_message(e)
        else:
            message = '不明なエラーが発生しました。詳細はログを確認してください。'
        
        # メッセージを出力し返却
        self.writeline_error(message)
        return message

import sys
sys.modules[__name__] = _LogUtil()
