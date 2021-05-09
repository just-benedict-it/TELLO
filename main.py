from djitellopy import Tello
from time import sleep

me = Tello()

me.connect()
me.takeoff()

# me.move_left(30)
# sleep(1)
# me.move_right(50)
# sleep(1)
# me.rotate_counter_clockwise(90)
# sleep(1)
# me.send_rc_control(-10,0,0,0)
# sleep(2)
#
# me.send_rc_control(0,20,0,0)
# sleep(2)
# me.send_rc_control(0,-20,0,0)
sleep(3)
me.land()
