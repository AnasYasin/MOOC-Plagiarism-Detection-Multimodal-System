import cv2
import numpy as np      
import os
import sys

number_of_images = 3
dir_data = sys.argv[1] + '/'
sum_data_images = np.zeros((number_of_images,3))
for i in range(number_of_images):
    img_data = cv2.imread(dir_data + str(i+1) +'.png')
    scale = (img_data - img_data.min()) / (img_data.max() - img_data.min())
    sum_dataCh1 = np.sum(scale[:,:,0])
    sum_dataCh2 = np.sum(scale[:,:,1])
    sum_dataCh3 = np.sum(scale[:,:,2])        
    sum_data_images[i, 0] = sum_dataCh1
    sum_data_images[i, 1] = sum_dataCh2
    sum_data_images[i, 2] = sum_dataCh3

np.save('train_data.npy', sum_data_images)
