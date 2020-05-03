echo off

rem ディレクトリ移動
cd %~dp0

rem envファイル読み込み
call loadenv.bat env\python.env

rem 実行
C:\Users\%USERNAME%\%python% main.py

pause
