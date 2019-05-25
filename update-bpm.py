from spotify_current_track import SpotifyCurrentTrack
import time

# initialize track
track = SpotifyCurrentTrack()
track.get_token()
track.create_client()

# get track info for the first time
print('get track info for the first time')
track.get_track()
track.get_song_id()
track.get_bpm()
print('starting bpm is ')
print(track.bpm)

# save to file
bpm_file = open('bpm.txt', 'w')
bpm_file.write(str(track.bpm))
bpm_file.close()

# starting point for time last update
time_last_update = time.time()

while True:
    # check if 5 seconds have elapsed
    if time.time() - time_last_update > 5:
        # update bpm
        track.get_track()
        track.get_song_id()
        track.get_bpm()
        print('updated bpm to ')
        print(track.bpm)

        # save to file
        bpm_file = open('bpm.txt', 'w')
        bpm_file.write(str(track.bpm))
        bpm_file.close()

        # reset time last update
        time_last_update = time.time()
        print('reset time last update')
