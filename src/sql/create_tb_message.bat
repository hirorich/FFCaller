echo off

rem �f�B���N�g���ړ�
cd %~dp0
cd ..\

rem env�t�@�C���ǂݍ���
call env\loadenv.bat env\python.env
call conda activate %env%

rem ���s
if not exist "db" mkdir "db"
if exist ".\tb_message.txt" del ".\tb_message.txt"
if exist ".\db\cmn_db.sqlite3" del ".\db\cmn_db.sqlite3"
sqlite3 ./db/cmn_db.sqlite3 < ./sql/create_tb_message.sql

pause
