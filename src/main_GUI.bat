echo off

rem �f�B���N�g���ړ�
cd %~dp0

rem env�t�@�C���ǂݍ���
call loadenv.bat env\python.env

rem ���s
C:\Users\%USERNAME%\%python% main_GUI.py

pause
