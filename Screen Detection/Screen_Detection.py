import cv2
import numpy as np      
import os
from matplotlib import pyplot as plt
import sys

font = cv2.FONT_HERSHEY_SIMPLEX
training_imgs = 7

def predict(train_data, img_pred):
    scale = (img_pred - img_pred.min()) / (img_pred.max() - img_pred.min())

    sum_predCh1 = np.sum(scale[:,:,0])
    sum_predCh2 = np.sum(scale[:,:,1])
    sum_predCh3 = np.sum(scale[:,:,2])

    totaldiffCh1 = 0
    totaldiffCh2 = 0
    totaldiffCh3 = 0
    
    for i in range(training_imgs):
        totaldiffCh1 += abs(train_data[i,0] - sum_predCh1)
        totaldiffCh2 += abs(train_data[i,1] - sum_predCh2)
        totaldiffCh3 += abs(train_data[i,2] - sum_predCh3)

    totaldiffCh1 /= training_imgs
    totaldiffCh2 /= training_imgs
    totaldiffCh3 /= training_imgs

    return totaldiffCh1, totaldiffCh2, totaldiffCh3


if __name__ == "__main__":
    
    train_data = np.load('train_data.npy')
    videoName = sys.argv[1]
    video = cv2.VideoCapture(videoName)
    fps = 25
    flow = 0
    continueFlow = 0    
    timeForPlag = 3 #in seconds
    while(video.isOpened()):
        ret, img_pred = video.read()
        
        if ret == True: #checking for if there are more frames left in video
            val1, val2, val3 = predict(train_data, img_pred)
            flow+=1 
            if (val1 > 29000 or len(str(int(val2))) > 5 or len(str(int(val3))) > 5):
                continueFlow+=1
                #print(": PLAG", val1, ' | ' ,  val2, ' | ' , val3)
                cv2.putText(img_pred, 'PLAG', (700,300), font, 3, (0, 0, 255), 2, cv2.LINE_AA)
            else:
                #print(": No PLAG", val1, ' | ' ,  val2, ' | ' , val3)
                cv2.putText(img_pred, 'NO PLAG', (700,300), font, 3, (0, 255, 0), 2, cv2.LINE_AA)
                continueFlow = 0
                flow = 0
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cv2.imshow('Frame',img_pred)
            if (flow == continueFlow and (flow > (fps*timeForPlag))):
                print("Plag")
 
        else: #end of video
            break
