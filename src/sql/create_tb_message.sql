/* メッセージTBL作成 */
/*
if not exist "db" mkdir "db"
call loadenv.bat env\python.env
call conda activate %env%
sqlite3 ./db/cmn_db.sqlite3 < ./sql/create_tb_message.sql
*/

/* メッセージTBL作成 */
create table tb_message (
	id text not null, -- メッセージID
	message text not null, -- メッセージ内容
	primary key (
		id
	)
);

/* メッセージ追加 */
insert into tb_message (id, message) values ('I0000000', '情報メッセージ');
insert into tb_message (id, message) values ('E0000000', 'エラーメッセージ');
insert into tb_message (id, message) values ('W0000000', '警告メッセージ');

/* 出力用に設定 */
.mode column
.headers on
.output ./tb_message.txt

/* メッセージTBLの内容をファイルに出力 */
select id, message, del_flg from tb_message order by id;

/* 標準出力に戻す */
.output stdout

/* 終了 */
.exit
