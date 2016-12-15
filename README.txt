### How to install Classifier ###


1) Download All files from links as shown below or GitHub repo. 

OneDrive : https://1drv.ms/u/s!AsgJ-NdXPSPKhXdfJLT7JZY4WKwC
Mirror #1 : http://medicalphoto.org/deep.zip
Mirror #2 : http://sshan.dynu.com/file/deep.zip
Mirror #3 : http://daoc.dynu.com/file/deep.zip

cf) DO NOT DIRECTLY DOWNLOAD FROM DOWNLOAD-ZIP ICON FROM GITHUB; Due to LFS issues of github, caffemodel files will not be downloaded correctly. If you want to download via Github, you must use GitHub Desktop(https://desktop.github.com/)


2) Run .bat files

100(typical)-hallym;caffenet.bat
100(typical)-hallym;resnet.bat
100(typical)-web;caffenet.bat
100(typical)-web;resnet.bat
100(typical+atypical)-hallym;caffenet.bat
100(typical+atypical)-hallym;resnet.bat
100(typical+atypical)-web;caffenet.bat
100(typical+atypical)-web;resnet.bat


3) DEMO website : http://dx.medicalphoto.org  (ResNet-152 trained with 100(typical)Asan dataset)



# About /dist/predict/predict.exe

- It requires 64 bit Windows.
- It requires MSVC 2013 redistribution libraries(/dist/vcredist_x64.exe). It will be silently installed by DOS batch scripts. 
- Examples of predict.exe usage 
predict.exe 227 caffe_deploy.prototxt caffe.caffemodel test_folder mean_label_folder "Memo" 
predict.exe 224 resnet152_deploy.prototxt resnet152.caffemodel test_folder mean_label_folder "Memo"
- The outputs will be saved in Report.txt.
- predict.exe compare the output of CNN and the directory name of test_folder.
- mean_label_folder should contains label.txt and meanOOOxOOO.binaryproto file.

# About /src/predict.py

- Python source code of Predict.exe
- PyCaffe should be installed first. (http://caffe.berkeleyvision.org/installation.html)
