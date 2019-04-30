import cv2
import numpy as np

newList = []
num = 18
# frames = [];
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
for i in range(num):
    rgb = cv2.imread('blur/%d.png'%i)
    newList.append(rgb)

resHeight, resWidth, c = newList[0].shape
video = cv2.VideoWriter('blurred.mov', fourcc, fps = 10, frameSize = (resWidth, resHeight), isColor = 1)

for ff in newList:
    video.write(ff)