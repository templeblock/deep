@echo off
echo "%PROCESSOR_ARCHITECTURE%"
if "%PROCESSOR_ARCHITECTURE%"=="AMD64" goto 64BIT
echo Windows Caffe does not support 32bit Windows 
pause
goto END
:64BIT
echo Install MSVC libraries... wait... 
%cd%\dist\vcredist_x64.exe /quiet /norestart
%cd%\dist\predict\predict.exe 224 %cd%/models/resnet_deploy.prototxt %cd%/models/resnet/100(typical)-web/res_runiter5_final-5_resnet_152_iter_8800.caffemodel %cd%/test_hallym %cd%/models/resnet/100(typical)-web "Traning : Asan(typical) ; Testing : hallym ; ResNet-152" 
pause
:END
