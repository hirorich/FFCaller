echo off

rem ディレクトリ移動
cd %~dp0

rem envファイル読み込み
call ..\src\env\loadenv.bat env\icon.env
call conda activate %env%

rem 実行
python icon.py

pause
