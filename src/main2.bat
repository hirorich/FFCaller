echo off

rem �f�B���N�g���ړ�
cd %~dp0

rem env�t�@�C���ǂݍ���
call loadenv.bat env\python.env
call conda activate %env%

rem DB�o�^
if exist .\tb_message.txt del .\tb_message.txt
if not exist "db" mkdir "db"
if exist .\db\cmn_db.sqlite3 del .\db\cmn_db.sqlite3
sqlite3 ./db/cmn_db.sqlite3 < ./sql/create_tb_message.sql

rem ���s
python main2.py

pause
