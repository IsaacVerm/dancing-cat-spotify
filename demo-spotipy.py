import spotipy
import spotipy.util as util

client_id = 'f8484dbf6f3543cf9bceba7a59709cb8'
client_secret = '596da43e1309493a92bd67aa94c0e2b5'

token = util.oauth2.SpotifyClientCredentials(
    client_id, client_secret)

cache_token = token.get_access_token()

spotify = spotipy.Spotify(cache_token)

results = spotify.current_user_playing_track()
print(results)
