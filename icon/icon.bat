echo off

rem ディレクトリ移動
cd %~dp0

rem envファイル読み込み
call ..\env\loadenv.bat ..\env\python.env
call conda activate %env%

rem 実行
python icon.py

rem アイコン作成
magick ./icon_512x512.png -define icon:auto-resize ./icon.ico
copy /Y .\icon.ico ..\web\icon

