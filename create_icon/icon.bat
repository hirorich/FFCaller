echo off

rem �f�B���N�g���ړ�
cd %~dp0

rem env�t�@�C���ǂݍ���
call ..\src\env\loadenv.bat ..\src\env\python.env
call conda activate %env%

rem �t�H���_�쐬
if not exist icon mkdir icon
del /Q icon\*

rem ���s
python icon.py

rem �A�C�R���쐬
convert ./icon/icon_512x512.png -define icon:auto-resize ./icon/icon.ico

