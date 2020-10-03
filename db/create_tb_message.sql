/* メッセージTBL作成 */
/*
sqlite3 ./cmn_db.sqlite3 < ./create_tb_message.sql
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
insert into tb_message (id, message) values ('E0000000', 'エラーメッセージ');
insert into tb_message (id, message) values ('E0000001', '入力ファイルが指定されていません');
insert into tb_message (id, message) values ('E0000002', '指定したファイルが存在しません(%0)');
insert into tb_message (id, message) values ('E0000003', '%0は%1以上を入力してください(%2)');
insert into tb_message (id, message) values ('E0000004', '%0は%1以下を入力してください(%2)');
insert into tb_message (id, message) values ('E0000005', '%0は%1以上%2以下を入力してください(%3)');
insert into tb_message (id, message) values ('E0000006', '映像有無が混在するため結合できません');
insert into tb_message (id, message) values ('E0000007', '音声有無が混在するため結合できません');
insert into tb_message (id, message) values ('E0000008', '動画ストリームが存在しないためフレーム数指定はできません(%0)');
insert into tb_message (id, message) values ('E0000009', '動画ストリームが存在しないためフレーム分割はできません(%0)');
insert into tb_message (id, message) values ('I0000000', '情報メッセージ');
insert into tb_message (id, message) values ('W0000000', '警告メッセージ');

/* 出力用に設定 */
.mode column
.headers on
.output ./tb_message.txt

/* メッセージTBLの内容をファイルに出力 */
select id, message from tb_message order by id;

/* 標準出力に戻す */
.output stdout

/* 終了 */
.exit
