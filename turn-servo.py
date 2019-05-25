from gpiozero import AngularServo
import time
from time import sleep

# initialize servo
servo = AngularServo(17, min_angle=-20, max_angle=20)

# read bpm for the first time
bpm_file = open('bpm.txt', 'r')
bpm = float(bpm_file.read())
bpm_file.close()

# starting point for time last update
time_last_update = time.time()

while True:
    # get updated value of written bpm every 5 seconds
    if time.time() - time_last_update > 5:
        # read bpm again
        bpm_file = open('bpm.txt', 'r')
        bpm = float(bpm_file.read())
        bpm_file.close()

        # reset time last update
        time_last_update = time.time()

    # rotate servo on the beat of the music
    servo.angle = -20
    sleep(60/bpm)
    servo.angle = 20
    sleep(60/bpm)
