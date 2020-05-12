# ==================================================
# ビジネスエラー部品
# ==================================================

from common.utility import message_utils

# ビジネスエラークラス
class BusinessError(Exception):
    
    # IDを基にメッセージ設定
    def set_business_error_message(self):
        self.args = (self.get_business_error_message(), )
    
    # IDを基にメッセージ取得
    def get_business_error_message(self):
        
        try:
            
            # メッセージ指定チェック
            if len(self.args) == 0:
                return 'エラーメッセージ未指定'
            
            # メッセージIDとパラメータ取得
            message_id = self.args[0]
            if len(self.args) >= 2:
                message_args = self.args[1:]
            else:
                message_args = None
            
            # メッセージ取得
            return message_utils.get_message(message_id, message_args)
            
        except:
            # 例外が発生した場合はメッセージ取得に失敗した旨を返却
            return 'エラーメッセージの取得失敗'

