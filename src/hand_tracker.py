import cv2
import mediapipe as mp
import time

captured = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands()

prevTime = 0
currentTime = time.time()

while True:
    success, img = captured.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img)

    # Getting the hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, landmark in enumerate(hand_landmarks.landmark):
                height, width, channel = img.shape
                center_x, center_y = int(landmark.x*width), int(landmark.y*height)
                print(f"{id}. x={center_x} y={center_y}")
                
                # Uncomment the following lines of code and replace 'n' with any number from 0-20
                # if id == n :
                #     cv2.circle(img, (center_x, center_y), 15, (0, 0, 0), cv2.FILLED)
                
            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)

    # Framerate Calculation
    currentTime = time.time()
    fps = 1/(currentTime-prevTime)
    prevTime = currentTime
    cv2.putText(img, "FPS : "+str(int(fps)), (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 0), 2)

    # Displaying the image
    cv2.imshow("Camera", img)
    cv2.waitKey(1)