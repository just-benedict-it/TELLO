from djitellopy import tello
import keyboard as kp
from time import sleep
import numpy as np
import cv2
import math

kp.init()
# me = tello.Tello()
# me.connect()
# print(me.get_battery())

#############parameters###############
x, y = 500, 500

fSpeed = 120/10
aSpeed = 360/10
interval = 0.25

a = 0
yaw = 0

dInterval = fSpeed*interval
aInterval = aSpeed*interval

points = []

def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50
    d = 0
    global x, y, yaw, a

    if kp.getKey('LEFT'):
        lr = -speed
        d = dInterval
        a = -180

    elif kp.getKey('RIGHT'):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey('UP'):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey('DOWN'):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey('w'):
        ud = speed

    elif kp.getKey('s'):
        ud = -speed

    if kp.getKey('a'):
        yv = -speed
        yaw -= aInterval

    elif kp.getKey('d'):
        yv = speed
        yaw += aInterval

    # if kp.getKey("q") : me.land()
    # if kp.getKey("e") : me.takeoff()

    sleep(interval)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]

def drawCircles(img, points):
    for point in points:
        cv2.circle(img, point ,5,(0,0,255), cv2.FILLED)
    cv2.putText(img, f"({(points[-1][0]-500)/100}, {(points[-1][1]-500)/100})m",
                (points[-1][0]+10, points[-1][1]+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)


while True:
    vals = getKeyboardInput()
    # me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    points.append((vals[4], vals[5]))

    img = np.zeros((1000,1000,3), np.uint8)
    drawCircles(img, points)
    cv2.imshow("Output",img)
    cv2.waitKey(1)

