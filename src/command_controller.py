import cv2
import os
import subprocess

import hand_tracker as ht

class CommandController:
    def __init__(self) -> None:
        self.system = os.name
        self.tracker = ht.HandTracker(maxHands=1)
        self.fingers = list()
        
    def get_open_fingers(self):
        self.fingers = list()
        if len(self.lmList):
            for tip in range(4, 21, 4):
                if tip == 4:
                    if self.lmList[tip][1] < self.lmList[tip-2][1]:
                        self.fingers.append(1)
                    else:
                        self.fingers.append(0)
                else:
                    if self.lmList[tip][2] < self.lmList[tip-2][2]:
                        self.fingers.append(1)
                    else:
                        self.fingers.append(0)
    
    def execute_command(self):
        self.get_open_fingers()
        
        if self.fingers == [0, 1, 0, 0, 1]:
            if self.system.lower() == "nt":
                proccess = subprocess.Popen(["C:/Users/neetu\Desktop/Saketh's Stuff/Gesture_Recognition/src/commands/command1.bat"])
                proccess.wait()
            else:
                subprocess.call(["sh", "src/commands/command1.sh"])
    
    def run(self):
        cap = cv2.VideoCapture(1)
        while True:
            success,img = cap.read()
            img = self.tracker.handsFinder(img)
            self.lmList = self.tracker.positionFinder(img)
            cv2.imshow("Video",img)
            if cv2.waitKey(5) & 0xFF == ord('q'):
                cap.release()
            self.execute_command()
            cv2.waitKey(1)
            
if __name__ == "__main__":
    cc = CommandController()
    cc.run()