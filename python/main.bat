echo off

rem ディレクトリ移動
cd %~dp0

rem envファイル読み込み
call loadenv.bat env\python.env

rem ワークフォルダ作成
if not exist "_output" mkdir "_output"
if not exist "_output\frame" mkdir "_output\frame"
del /q "_output\frame\*"
if not exist "_output\video" mkdir "_output\video"
del /q "_output\video\*"

rem 実行
C:\Users\%USERNAME%\%python% main.py


rem メモ
rem N = 10^4
rem a [秒] => ceiling(a * fps) + 1 [フレーム]
rem b [フレーム] => floor(N * (a - 1) / fps)/ N [秒]

pause
