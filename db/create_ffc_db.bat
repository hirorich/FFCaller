echo off

rem ディレクトリ移動
cd %~dp0
cd ..\

rem envファイル読み込み
call env\loadenv.bat env\python.env
call conda activate %env%

rem 実行
if exist ".\db\ffc_db.sqlite3" del ".\db\ffc_db.sqlite3"
sqlite3 ./db/ffc_db.sqlite3 < ./db/create_ffc_db.sql

pause
