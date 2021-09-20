import cv2 as cv

img = cv.imread('D:\OpenCV\Basics\photos\me.jpg')

resize = cv.resize(img, (550, 550), interpolation=cv.INTER_AREA)
cv.imshow('resize', resize)

gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(resize, (7,7),sigmaX=5, borderType=cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

edge = cv.Canny(resize, threshold1=125, threshold2=115)
cv.imshow('edge', edge)

dilation = cv.dilate(edge, (3,3), iterations=2)
cv.imshow('dilate', dilation)

erosion = cv.erode(dilation, (3,3), iterations=2)
cv.imshow('erose', erosion)

crop = resize[30:350, 70:400]
cv.imshow('cropped', crop)

cv.waitKey(0)
