'''
Title           :make_predictions_1.py
Description     :This script makes predictions using the 1st trained model and generates a submission file.
Author          :Adil Moujahid
Date Created    :20160623
Date Modified   :20160625
version         :0.2
usage           :python make_predictions_1.py
python_version  :2.7.11
'''
import datetime,time
import sys
import os
import glob
import cv2
import caffe
import lmdb
import numpy as np
from caffe.proto import caffe_pb2
from shutil import copyfile

#os.environ['GLOG_minloglevel']='3'

if (len(sys.argv)<6):
    print 'Usage : predict.exe(or python predict.py) \"Image_width&height\" \"deploy file\" \"Model file(.caffemodel)\" \"Test folder\" \"folder containing 1) meanOOOxOOO.binaryproto 2) label.txt\" \"Memo\"'
    exit(1)

caffe.set_mode_cpu()

#Size of images
IMAGE_WIDTH = int(sys.argv[1])
IMAGE_HEIGHT = int(sys.argv[1])

'''
Image processing helper function
'''
def printout(text):
    global printpath
    f = open(printpath,'a')
    f.write(text + '\n')
    print text
    f.close()
    return

def transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT):

    #Histogram Equalization
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
    img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])

    #Image Resizing
    img = cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_CUBIC)
    return img


printpath = "report.txt"
default_test_path='/home/ai/data/test'
if (len(sys.argv)>4):
    default_test_path=str(sys.argv[4])


datapath = "/home/ai/cat/input"

printout('\n### Start Analysis ###')
if (len(sys.argv)>5):
    printout('# Mean binary(mean.binaryproto) & label file(label.txt) folder : ' + str(sys.argv[5]))
    data_path=str(sys.argv[5])

printout('# Model(.caffemodel) file : ' + str(sys.argv[3]))
printout('# Test photographs folder : ' + default_test_path)
'''
Reading mean image, caffe model and its weights 
'''
#Read mean image
mean_blob = caffe_pb2.BlobProto()
with open(data_path+ '/mean'+ str(sys.argv[1]) + 'x' + str(sys.argv[1]) +'.binaryproto','rb') as f:
    mean_blob.ParseFromString(f.read())
mean_array = np.asarray(mean_blob.data, dtype=np.float32).reshape(
    (mean_blob.channels, mean_blob.height, mean_blob.width))

list_dx = []

print data_path+'/label.txt'
f=open(data_path+'/label.txt')
list_dx=f.read().splitlines()
f.close()
print 'Label.txt : '
print list_dx
#Read model architecture and trained model's weights
net = caffe.Net(str(sys.argv[2]),
                str(sys.argv[3]),
                caffe.TEST)
#Define image transformers
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', mean_array)
transformer.set_transpose('data', (2,0,1))

'''
Making predicitions
'''
#Reading image paths
test_img_paths=[]
for root,dirs,files in os.walk(default_test_path):
    for fname in files:
        ext=(os.path.splitext(fname)[-1]).lower()
        if ext == ".jpg" or ext == ".jpeg" or ext == ".gif" or ext == ".png" : test_img_paths+=[os.path.join(root,fname)]


#Making predictions
test_ids = []
preds = []

#list_dx = ['wart','lentigo','sebk','bcc']
blank_list =[]
for i in range(len(list_dx)):
    blank_list.append(0)

mis_dx=[]
for i in range(len(list_dx)):
    mis_dx.append(list(blank_list))

correct_dx = list(blank_list)
correct2_dx = list(blank_list)
total_dx = list(blank_list)
correct=0
correct2=0
total_c=0

#os.system('rm -rf  /home/ai/data/error')
#os.system('mkdir /home/ai/data/error')
for img_path in test_img_paths:
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    if img is None :
        continue
    img = transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT)
    
    net.blobs['data'].data[...] = transformer.preprocess('data', img)
    out = net.forward()
    pred_probas = out['prob']

    test_ids = test_ids + [img_path.split('/')[-1][:-4]]
    preds = preds + [pred_probas.argmax()]

    result_tuple=[]
    for i,p_ in enumerate(pred_probas[0]):
        result_tuple+=[(round(p_*100),i)]
    result_tuple=sorted(result_tuple)
    result_tuple.reverse()

    printtxt=""
    for result_ in result_tuple:
        printtxt='%s [%s %d] ' % (printtxt,list_dx[result_[1]],result_[0])
    printout(printtxt + '  : ' + img_path)

    max1=0.0
    max2=0.0
    max1_index=0
    max2_index=0
    for i,p_ in enumerate(pred_probas[0]):
        if (p_> max1):
            max1=p_
            max1_index=i
    for i,p_ in enumerate(pred_probas[0]):
        if (p_ > max2 and p_ < max1):
            max2=p_
            max2_index=i
    temp_correct=0
    for i,dx_ in enumerate(list_dx):
        if dx_ in os.path.dirname(img_path): 
            total_dx[i]+=1
            if max1_index == i: 
                temp_correct=1
                correct_dx[i]+=1
            else:
                mis_dx[i][max1_index]+=1
            if max2_index == i: 
                correct2+=1
                correct2_dx[i]+=1

    if temp_correct==1:
        correct+=1
#    else:
#        print img_path
#        result_=""
#        targetpath = '/home/ai/data/error/' +str(pred_probas.argmax()) +os.path.basename(img_path)
#        print '%s %d , %s %d' % (list_dx[max1_index],max1*100/sum(pred_probas[0],0.0),list_dx[max2_index],max2*100/sum(pred_probas[0],0.0))
#        os.system('cp \"%s\" \"%s\"' % (img_path, targetpath))
     

    total_c+=1       

printout('\n###result###')
if (len(sys.argv)>6):
    printout(str(sys.argv[6]))
printout('Top 1 : %d (%d / %d))' % (correct * 100 / total_c, correct, total_c))
printout('Top 2 : %d (%d / %d))' % ((correct + correct2) * 100 / total_c, (correct + correct2), total_c))

for i,dx_ in enumerate(list_dx):
    if total_dx[i]>0:
        printout('\n' + dx_)
        printout('Top1 : %d / %d = %d percent' % (correct_dx[i],total_dx[i], correct_dx[i] * 100 / total_dx[i]))
        printout('Top2 : %d / %d = %d percent' % (correct_dx[i]+correct2_dx[i],total_dx[i], (correct_dx[i]+correct2_dx[i]) * 100 / total_dx[i]))
        max3=0
        for j,p_ in enumerate(mis_dx[i]):
            if (p_ > max3):
                max3=p_
                max3_index=j
        if (sum(mis_dx[i],0.0)>0) : printout('MissDx  %s (%d percent) ' % (list_dx[max3_index],max3 * 100 /sum(mis_dx[i],0.0)))

printout('\n### Analysis Finished ###\n')
