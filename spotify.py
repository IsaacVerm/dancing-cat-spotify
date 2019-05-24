from config import *
import spotipy
import spotipy.util as util


def get_currently_playing_track():
    token = util.prompt_for_user_token(
        USERNAME, SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

    spotify = spotipy.Spotify(token)

    return spotify.current_user_playing_track()


print(get_currently_playing_track())
