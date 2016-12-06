Windows classifier - predict.exe

- It requires 64 bit Windows.
- It requires MSVC 2013 redistribution libraries. It will be silently installed by scripts. (/dist/vcredist_x64.exe)

example)
predict.exe 227 caffe_deploy.prototxt caffe.caffemodel test_folder mean_label_folder "Memo" 
predict.exe 224 resnet152_deploy.prototxt resnet152.caffemodel test_folder mean_label_folder "Memo"

- The outputs will be saved in Report.txt.
- predict.exe compare the output of CNN and the directory name of test_folder.
- mean_label_folder should contains label.txt and meanOOOxOOO.binaryproto file.