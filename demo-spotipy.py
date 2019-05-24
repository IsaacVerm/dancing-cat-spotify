import spotipy
import spotipy.util as util

username = ''
scope = ''
client_id = 'f8484dbf6f3543cf9bceba7a59709cb8'
client_secret = '596da43e1309493a92bd67aa94c0e2b5'
redirect_uri = 'http://localhost/'

token = util.oauth2.SpotifyClientCredentials(
    client_id, client_secret)

cache_token = token.get_access_token()

spotify = spotipy.Spotify(cache_token)

results = spotify.search(q='artist:' + 'cobain', type='artist')
print(results)
