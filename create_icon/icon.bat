echo off

rem �f�B���N�g���ړ�
cd %~dp0

rem env�t�@�C���ǂݍ���
call ..\src\env\loadenv.bat env\icon.env
call conda activate %env%

rem ���s
python icon.py

pause
