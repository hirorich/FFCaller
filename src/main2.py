# sqlite3のインポート
import sqlite3

# 
def create_message(message_id):
    
    db_filename = './db/cmn_db.sqlite3'
    
    with sqlite3.connect(db_filename) as conn:
        
        cursor = conn.cursor()
        
        query = "select id, message from tb_message where id = ?"
        
        cursor.execute(query, (message_id,))
        
        list1 = cursor.fetchone()
        
        print(message_id)
        print(list1[1].replace('%0', 'AA').replace('%1', 'あい').replace('%2', '上限').replace('%3', '0%09'))

# main
if __name__ == "__main__":
        
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
    
