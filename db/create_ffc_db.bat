echo off

rem �f�B���N�g���ړ�
cd %~dp0
cd ..\

rem env�t�@�C���ǂݍ���
call env\loadenv.bat env\python.env
call conda activate %env%

rem ���s
if exist ".\db\ffc_db.sqlite3" del ".\db\ffc_db.sqlite3"
sqlite3 ./db/ffc_db.sqlite3 < ./db/create_ffc_db.sql

pause
