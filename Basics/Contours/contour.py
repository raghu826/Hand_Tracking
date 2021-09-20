import numpy as np
import cv2

img = cv2.imread('D:\OpenCV\photos\me.jpg')
resized = cv2.resize(img, (512,512), cv2.INTER_AREA)
imgray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))


cv2.drawContours(resized, contours, 1, (0, 255, 0), 3)
#cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', resized)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
