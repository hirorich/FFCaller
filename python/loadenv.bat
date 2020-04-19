echo off

REM 設定ファイルが存在するか確認する
if not exist %1 (
    echo ERROR: Not found %1
    exit /b 1
)

REM 設定ファイルを読み込む
for /f "usebackq tokens=1,* delims==" %%a in ("%1") do (
    set %%a=%%b
)

exit /b 0
