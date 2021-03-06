from spotify_current_track import SpotifyCurrentTrack

from gpiozero import AngularServo
import time
from time import sleep
servo = AngularServo(17, min_angle=-20, max_angle=20)

# setup
time_last_update = time.time()
nr_iterations = 0

# initialize track
track = SpotifyCurrentTrack()
track.get_token()
track.create_client()

while True:
    # get track info for the first time
    if nr_iterations == 0:
        print('get track info for the first time')
        track.get_track()
        track.get_song_id()
        track.get_bpm()
        print('bpm is ')
        print(track.bpm)

        nr_iterations += 1

    # check if 5 seconds have elapsed
    if time.time() - time_last_update > 5:
        # update bpm
        track.get_track()
        track.get_song_id()
        track.get_bpm()
        print('updated bpm to ')
        print(track.bpm)

        # reset time last update
        time_last_update = time.time()
        print('reset time last update')

    # rotate servo on the beat of the music
    servo.angle = -20
    sleep(60/track.bpm)
    servo.angle = 20
    sleep(60/track.bpm)
