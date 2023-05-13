import cv2
import os
import subprocess

import mysql.connector

import hand_tracker as ht

class CommandController:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(user="saketh", password="notpassword", host="localhost", database="smartges")
        self.cursor = self.connection.cursor()

        self.cursor.execute("select * from gestures")
        self.commands = self.cursor.fetchall()
        self.connection.close()

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

        for cmd in self.commands:
            code = ''.join(str(i) for i in self.fingers)
            if code == cmd[0]:
                try:
                    if self.system.lower() == "nt":
                        proccess = subprocess.Popen([f"C:/Users/neetu/Desktop/Saketh's Stuff/Gesture_Recognition/src/commands/{cmd[1]}.bat"])
                        proccess.wait()
                    else:
                        subprocess.call(["sh", f"src/commands/{cmd[1]}.sh"])
                except:
                    print("file not found")
    
    def run(self):
        cap = cv2.VideoCapture(1)
        while True:
            success,img = cap.read()
            img = self.tracker.handsFinder(img)
            self.lmList = self.tracker.positionFinder(img)
            cv2.imshow("Video",img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                break
            cv2.waitKey(1)
            self.execute_command()
            
if __name__ == "__main__":
    cc = CommandController()
    cc.run()
