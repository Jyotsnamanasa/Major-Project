import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import requests
import pyttsx3
import time
import pickle
# from PIL import ImageGrab
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()

encodeListKnown=[]
classNames=[]
def findEncodings(images):
    
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def train():
    
    path = 'Training_images'
    images = []
    
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    encodeListKnown = findEncodings(images)
    all_face_encodings=dict(zip(classNames,encodeListKnown))
    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(all_face_encodings, f)
    print('Encoding Complete')
    #return encodeListKnown
#print(classNames)




def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()


        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr

#encodeListKnown = findEncodings(images)

#print('Encoding Complete')
def detect():
    with open("dataset_faces.dat","rb") as f:
        all_face_encodings=pickle.load(f)
    
    #url="http://[2401:4900:60db:5b74:988e:7a0f:58:35c5]:8080/video"
    cap = cv2.VideoCapture(0)
    
    
    classNames= list(all_face_encodings.keys())
    encodeListKnown=np.array(list(all_face_encodings.values()))
    while True:
        success, img = cap.read()
    # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        #cv2.imshow("img",imgS)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            
                
    # print(faceDis)
            matchIndex = np.argmin(faceDis)
            prob=(1-faceDis[matchIndex])*100
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
            print(faceDis[matchIndex])
            if faceDis[matchIndex]>0.5:
                name='Unknown'
    # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
            #markAttendance(name)
            print(name)
            if name!='Unknown':
                speak("Done!")
                time.sleep(3)
                
            

        cv2.imshow('Webcam', img)
        cv2.moveWindow('Webcam',400,100)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    cv2.destroyAllWindows()
key=0
while(key!=-1):
    #l=[train(),detect()]
    print("press 1 for Training \n\t2 for detection \n\t -1 for exit")
    key=int(input())
    if key==-1:
        break
    elif key>2 or key<-1:
        print("invalid key")
    else:
        if key==1:
            train()
        elif key==2:
            detect()
    
#train()