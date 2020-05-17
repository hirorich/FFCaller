echo off

rem ディレクトリ移動
cd %~dp0

rem envファイル読み込み
call ..\src\env\loadenv.bat ..\src\env\python.env
call conda activate %env%

rem フォルダ作成
if not exist icon mkdir icon
del /Q icon\*

rem 実行
python icon.py

rem アイコン作成
convert ./icon/icon_512x512.png -define icon:auto-resize ./icon/icon.ico

