echo off

rem �f�B���N�g���ړ�
cd %~dp0

rem env�t�@�C���ǂݍ���
call loadenv.bat env\python.env

rem ���[�N�t�H���_�쐬
if not exist "_output" mkdir "_output"
if not exist "_output\frame" mkdir "_output\frame"
del /q "_output\frame\*"
if not exist "_output\video" mkdir "_output\video"
del /q "_output\video\*"

rem ���s
C:\Users\%USERNAME%\%python% main.py


rem ����
rem N = 10^4
rem a [�b] => ceiling(a * fps) + 1 [�t���[��]
rem b [�t���[��] => floor(N * (a - 1) / fps)/ N [�b]

pause
