import cv2
import numpy as np
import hand_tracker as htm
import time
import pyautogui
 
wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
smoothening = 7
 
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
 
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.HandTracker(maxHands=1)
wScr, hScr = pyautogui.size()
 
while True:
    success, image = cap.read()
    image = detector.handsFinder(image)
    lmList, bbox = detector.positionFinder(image)
    
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:] #index finger
        x2, y2 = lmList[12][1:] #middle finger
    
    # 3. Check which fingers are up
    fingers = detector.fingersUp()
    cv2.rectangle(image, (frameR, frameR), (wCam - frameR, hCam - frameR),
    ((255, 255, 0)), 2)
    # 4. Only Index Finger : Moving Mode
    if fingers[1] == 1 and fingers[2] == 0:
        # 5. Convert Coordinates
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        # 6. Smoothen Values
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening
    
        # 7. Move Mouse
        pyautogui.moveTo(wScr - clocX, clocY)
        cv2.circle(image, (x1, y1), 15, ((255, 255, 0)), cv2.FILLED)
        plocX, plocY = clocX, clocY
        
    # 8. Both Index and middle fingers are up : Clicking Mode
    if fingers[1] == 1 and fingers[2] == 1:
        # 9. Find distance between fingers
        length, image, lineInfo = detector.findDistance(8, 12, image)
        print(length)
        # 10. Click mouse if distance short
        if length < 40:
            cv2.circle(image, (lineInfo[4], lineInfo[5]),
            15, (255, 255, 255), cv2.FILLED)
            pyautogui.click()
    
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(image, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    (255, 0, 0), 3)

    cv2.imshow("Image", image)
    cv2.waitKey(1)