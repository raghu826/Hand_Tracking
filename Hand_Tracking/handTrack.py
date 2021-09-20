import cv2 as cv
import mediapipe as mp
import time

# To capture webcam
cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# to access fps(frames per second)
start = 0
end = 0

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # mediapipe deals with RGB images
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            for index, lm in enumerate(hand.landmark):
                # print(index, lm)
                h, w, c = img.shape
                # centers of Landmark Points
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(index, cx, cy)
                #if index == 12:
                cv.circle(img, (cx, cy), 8, (0,255,0), -1)
                mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)

    end = time.time()
    fps = 1/(end-start)
    start = end

    cv.putText(img, 'FPS: {}'.format(int(fps)), (10,70), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 3)

    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()