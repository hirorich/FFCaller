echo off

rem �f�B���N�g���ړ�
cd %~dp0

rem env�t�@�C���ǂݍ���
call env\loadenv.bat env\logo.env
call conda activate %env%

rem ���s
python logo.py

pause
