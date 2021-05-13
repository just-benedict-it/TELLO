import cv2
from djitellopy import tello
import numpy as np

# me = tello.Tello()
cap = cv2.VideoCapture(0)
fbRange = [6200,6800]
pError = 0
w, h = 360,240
pid = [0.4,0.4,0]

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Recources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFacelistC = []
    myFacelistArea = []

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
        cx = x+w//2
        cy = y+h//2
        area = w*h
        cv2.circle(img, (cx, cy), 5,(0,255,0), cv2.FILLED )
        myFacelistC.append([cx,cy])
        myFacelistArea.append(area)

    if len(myFacelistArea) != 0:
        i = myFacelistArea.index(max(myFacelistArea))
        return img, [myFacelistArea[i], myFacelistC[i]]
    else:
        return img, [0,[0,0]]


def trackFace(info, w, pid, pError):
    fb = 0
    area = info[0]
    x,y = info[1]

    error = x-w//2
    speed = pid[0]*error + pid[1]*(error-pError)
    speed = int(np.clip(speed, -100,100))
    if area>fbRange[0] and area<fbRange[1]:
        fb =0
    elif area>fbRange[1]:
        fb =-20
    elif area<fbRange[0] and area !=0:
        fb=20

    if x==0:
        speed = 0
        error = 0

    print(speed, fb)
    # me.send_rc_control(0,fb,0,speed)
    return error


while True:
    _, img = cap.read()
    img = cv2.resize(img, (w, h))

    img, info = findFace(img)
    pError = trackFace(info, w, pid, pError)

    cv2.imshow('Output', img)
    print('Area', info[0], 'Center', info[1])
    cv2.waitKey(1)

