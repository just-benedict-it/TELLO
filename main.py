from djitellopy import Tello
from time import sleep

tello = Tello()

tello.connect()
tello.takeoff()

# tello.move_left(30)
# sleep(1)
# tello.move_right(50)
# sleep(1)
# tello.rotate_counter_clockwise(90)
# sleep(1)
# tello.send_rc_control(-10,0,0,0)
# sleep(2)
#
# tello.send_rc_control(0,20,0,0)
# sleep(2)
# tello.send_rc_control(0,-20,0,0)
sleep(3)
tello.land()
