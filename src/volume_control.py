import cv2
import time
import numpy as np
import math

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from hand_tracker import HandTracker as ht

cap = cv2.VideoCapture(0)
tracker = ht(detectionCon=0.75)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volume.GetVolumeRange()

volume.SetMasterVolumeLevel(-20.0, None)

while True:
    success, img = cap.read()
    img = tracker.handsFinder(img)
    lmList = tracker.positionFinder(img, draw=False)
    if len(lmList):
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        
        length = math.hypot(x2-x1, y2-y1)
        print(length)
    
    cv2.imshow("Camera", img)
    cv2.waitKey(1)