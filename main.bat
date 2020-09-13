echo off

rem ディレクトリ移動
cd %~dp0

rem envファイル読み込み
call env\loadenv.bat env\python.env
call conda activate %env%

rem 実行
python main.py

rem pause
