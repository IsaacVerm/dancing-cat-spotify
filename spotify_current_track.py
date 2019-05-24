from config import *
import spotipy
import spotipy.util as util


class SpotifyCurrentTrack:
    def get_token(self):
        self.token = util.prompt_for_user_token(
            USERNAME, SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

    def create_client(self):
        self.spotify_client = spotipy.Spotify(self.token)

    def get_track(self):
        self.current_track = self.spotify_client.current_user_playing_track()

    def get_song_id(self):
        self.song_id = self.current_track['item']['id']

    def get_bpm(self):
        audio_features = self.spotify_client.audio_features(
            tracks=[self.song_id])
        self.bpm = audio_features[0]['tempo']
        print(self.bpm)



