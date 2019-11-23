import cv2
import numpy as np      
import os
from matplotlib import pyplot as plt

def predict(dir_data, dir_pred):
    path, dirs, files = next(os.walk(dir_data))
    img_pred = cv2.imread(dir_pred)
    scale = (img_pred - img_pred.min()) / (img_pred.max() - img_pred.min())
    #img_pred = img_pred.flatten()

    sum_predCh1 = np.sum(scale[:,:,0])
    sum_predCh2 = np.sum(scale[:,:,1])
    sum_predCh3 = np.sum(scale[:,:,2])

    totaldiffCh1 = 0
    totaldiffCh2 = 0
    totaldiffCh3 = 0
    
    for i in range(len(files)):
        img_data = cv2.imread(dir_data + str(i+1) +'.png')
        scale = (img_data - img_data.min()) / (img_data.max() - img_data.min())
        sum_dataCh1 = np.sum(scale[:,:,0])
        sum_dataCh2 = np.sum(scale[:,:,1])
        sum_dataCh3 = np.sum(scale[:,:,2])        
        
        totaldiffCh1 += abs(sum_dataCh1 - sum_predCh1)
        totaldiffCh2 += abs(sum_dataCh2 - sum_predCh2)
        totaldiffCh3 += abs(sum_dataCh3 - sum_predCh3)

    totaldiffCh1 /= len(files)
    totaldiffCh2 /= len(files)
    totaldiffCh3 /= len(files)

    return totaldiffCh1, totaldiffCh2, totaldiffCh3


if __name__ == "__main__":
    dir_data = "sc/"
    dir_pred = "pred/1.png"
    val1, val2, val3 = predict(dir_data, dir_pred)
    
    for i in range(8):
        dir_pred = "pred/"
        dir_pred += str(i+1)+ ".png" 
        val1, val2, val3 = predict(dir_data, dir_pred)
        '''        
        print("R", val1)
        print("G", val2)
        print("B", val3)
        print("_______________________--")
        '''
        if (len(str(int(val1))) > 5 or len(str(int(val2))) > 5 or len(str(int(val3))) > 5):
            print(i+1, ": pledge")
        else:
            print(i+1, ": No pledge")
