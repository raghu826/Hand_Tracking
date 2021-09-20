import cv2 as cv

capture = cv.VideoCapture('D:\OpenCV\Basics\Videos\denmark.mp4')

while True:
    success, img = capture.read()
    cv.imshow('denmark', img)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()