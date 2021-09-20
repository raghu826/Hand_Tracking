import cv2 as cv
import numpy as np

dog = cv.imread('D:\OpenCV\Basics\photos\cat2.jpg')

# created a blank image
empty = np.zeros((512,512, 3), dtype='uint8')

#Drawing different shapes
cv.rectangle(empty, (0,0), (250,250), color = (230,180,150), thickness=-1)    #Rectangle
#cv.imshow('blank', empty)

cv.circle(empty, (250, 250), 50, color=(120, 50, 250), thickness=5)         #Circle
#cv.imshow('circle', empty)

cv.line(empty, (250, 250), (empty.shape[0], empty.shape[1]), color=(255, 255, 255), thickness=10)
cv.line(empty, (250, 250), (empty.shape[0], 0), color=(255, 255, 255), thickness=10)           #Line
cv.line(empty, (250, 250), (empty.shape[0], empty.shape[1]//2), color=(255, 255, 255), thickness=10)
#cv.imshow('line', empty)

cv.putText(empty, r'"I am a Devil of my word"', (25, 425),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1, color= (100, 150, 200), thickness=2)
cv.imshow('text', empty)

cv.waitKey(0)
