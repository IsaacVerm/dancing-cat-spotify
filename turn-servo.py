from gpiozero import AngugitlarServo
import time
from time import sleep

# initialize servo
servo_one = AngularServo(17, min_angle=-20, max_angle=20)
servo_two = AngularServo(27, min_angle=-20, max_angle=20)

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
    servo_one.angle = -20
    servo_two.angle = 20
    sleep(60/bpm)
    servo_one.angle = 20
    servo_two.angle = -20
    sleep(60/bpm)
