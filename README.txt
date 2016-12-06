### NOTICE ###
- If you download using Download ZIP icon, due to LFS issues of github, caffemodel files(/models/*) will not be downloaded correctly. Download the 4 caffemodel files one by one and overwrite to the folder or,

- Use OneDrive or mirror links.

OneDrive : https://1drv.ms/u/s!AsgJ-NdXPSPKhXc1yOuJFmXacfmN
Mirror #1 : http://medicalphoto.org/deep.zip
Mirror #2 : http://sshan.dynu.com/file/deep.zip
Mirror #3 : http://daoc.dynu.com/file/deep.zip



# Skin diseases(Basal cell carcinoma, seborrheic keratosis, lentigo, wart) classifier - predict.exe

- It requires 64 bit Windows.
- It requires MSVC 2013 redistribution libraries(/dist/vcredist_x64.exe). It will be silently installed by DOS batch scripts. 



# Examples of predict.exe usage 
predict.exe 227 caffe_deploy.prototxt caffe.caffemodel test_folder mean_label_folder "Memo" 
predict.exe 224 resnet152_deploy.prototxt resnet152.caffemodel test_folder mean_label_folder "Memo"

- The outputs will be saved in Report.txt.
- predict.exe compare the output of CNN and the directory name of test_folder.
- mean_label_folder should contains label.txt and meanOOOxOOO.binaryproto file.