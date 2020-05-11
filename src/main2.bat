echo off

rem ディレクトリ移動
cd %~dp0

rem envファイル読み込み
call loadenv.bat env\python.env
call conda activate %env%

rem DB登録
if exist .\tb_message.txt del .\tb_message.txt
if not exist "db" mkdir "db"
if exist .\db\cmn_db.sqlite3 del .\db\cmn_db.sqlite3
sqlite3 ./db/cmn_db.sqlite3 < ./sql/create_tb_message.sql

rem 実行
python main2.py

pause
