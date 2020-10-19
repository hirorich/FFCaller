echo off

rem ディレクトリ移動
cd %~dp0
cd ..\

rem envファイル読み込み
call env\loadenv.bat env\python.env
call conda activate %env%

rem 実行
if exist ".\db\cmn_db.sqlite3" del ".\db\cmn_db.sqlite3"
sqlite3 ./db/cmn_db.sqlite3 < ./db/create_tb_message.sql

pause
