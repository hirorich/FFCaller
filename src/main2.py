# sqlite3のインポート
import sqlite3

from common.utility import log_utils
from common.error.business_error import BusinessError

# 
def create_message(message_id):
    
    try:
        raise BusinessError(message_id, '引数0', 'ぱらめ1', 'パラメ2', 'param3')
    except Exception as e:
        log_utils.write_log(e)

# main
if __name__ == "__main__":
        
        create_message('A0000000')
        create_message('E0000000')
        create_message('E0000001')
        create_message('E0000002')
        create_message('E0000003')
        create_message('E0000004')
        create_message('E0000005')
        create_message('E0000006')
        create_message('E0000007')
        create_message('E0000008')
        create_message('E0000009')
        create_message('I0000000')
        create_message('W0000000')
        create_message('B0000000')
    
