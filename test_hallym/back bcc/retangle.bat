:treeProcess
rem Do whatever you want here over the files of this subdir, for example:
for %%f in (*.jpg) do (
c:\imagemagick\convert "%%f"   -set option:distort:viewport "%%[fx:min(w,h)]x%%[fx:min(w,h)]+%%[fx:max((w-h)/2,0)]+%%[fx:max((h-w)/2,0)]" -filter point -distort SRT 0  +repage "%%f"
)
for %%f in (*.jpeg) do (
c:\imagemagick\convert "%%f"   -set option:distort:viewport "%%[fx:min(w,h)]x%%[fx:min(w,h)]+%%[fx:max((w-h)/2,0)]+%%[fx:max((h-w)/2,0)]" -filter point -distort SRT 0  +repage "%%f"
)

for /D %%d in (*) do (
    cd %%d
    call :treeProcess
    cd ..
)
exit /b