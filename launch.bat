@ECHO OFF
SETLOCAL
PUSHD "%~dp0"

set /p top=specify where the bounding box starts (from the top of the screen): 
set /p left=specify where the bounding box starts (from the left of the screen): 
set /p width=enter width of the bounding box: 
set /p height=enter height of the bounding box: 

start                                   ^
    .\Runtime\App\Python\pythonw.exe    ^
    screen2vcam.py                      ^
    --top %top%                         ^
    --left %left%                       ^
    --width %width%                     ^
    --height %height%                   ^
    --preview

POPD
ENDLOCAL
@ECHO ON