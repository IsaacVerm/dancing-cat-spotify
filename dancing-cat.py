from spotify_current_track import SpotifyCurrentTrack

from gpiozero import Servo
from time import sleep

servo = Servo(17)
while True:
    # get bpm
    track = SpotifyCurrentTrack()
    track.get_token()
    track.create_client()
    track.get_track()
    track.get_song_id()
    track.get_bpm()

    # rotate servo on the beat of the music
    servo.min()
    sleep(60/track.bpm)
    servo.max()
    sleep(60/track.bpm)
