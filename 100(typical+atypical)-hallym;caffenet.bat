@echo off
echo "%PROCESSOR_ARCHITECTURE%"
if "%PROCESSOR_ARCHITECTURE%"=="AMD64" goto 64BIT
echo Windows Caffe does not support 32bit Windows 
pause
goto END
:64BIT
echo Install MSVC libraries... wait... 
%cd%\dist\vcredist_x64.exe /quiet /norestart
%cd%\dist\predict\predict.exe 227 %cd%/models/caffe_deploy.prototxt %cd%/models/caffenet/100(typical+atypical)-web/caffeperformance-6_model_2_iter_2451.caffemodel %cd%/test_hallym %cd%/models/caffenet/100(typical+atypical)-web "Traning : Asan(typical+atypical) ; Testing : hallym ; CaffeNet" 
pause
:END
