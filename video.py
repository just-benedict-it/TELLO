import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1/30)

    video.release()

#Thread 는 두 개 이상의 행동을 동시에 하기 위한 함수이다
#여기서는 tello를 움직이는 것과 recording을 동시에 수행하기 위해 사용했다
recorder = Thread(target =  videoRecorder)
recorder.start()

tello.takeoff()
tello.move_up(180)
tello.rotate_counter_clockwise(360)
tello.land()

keepRecording=False
#join 은 thread가 종료될 때까지 기다린다.
#keepRecording이 False가 아니면 계속 실행되겠지????
recorder.join()

