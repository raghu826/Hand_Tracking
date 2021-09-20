import cv2 as cv

# works well with the videos and webcam
def resize(img, scale):
    width = int(img.shape[0] * scale)
    height = int(img.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation= cv.INTER_AREA)


capture = cv.VideoCapture('D:\OpenCV\Basics\Videos\denmark.mp4')

while True:
    success, img = capture.read()
    newImg = resize(img, 0.15)
    cv.imshow('video', img)
    cv.imshow('resized video', newImg)

    if cv.waitKey(20) & 0xFF == ord('g'):
        break

capture.release()
cv.destroyAllWindows()