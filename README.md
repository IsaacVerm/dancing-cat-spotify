https://www.instructables.com/id/Servo-Motor-Control-With-Raspberry-Pi/

# Installation libraries

Normally the normal flow would be use `requirements.txt` to list the libraries to be installed using `pip install`. However, the latest version of `spotipy` is not available this way. This latest version contains methods like `current_user_playing_track` we need. Run the following to install the latest version of `spotipy` directly from GitHub:

```
pip install git+https://github.com/plamere/spotipy.git@master
```

# Authorization Spotify

Authorization to Spotify isn't that straightforward. The approach used mimics the one explained [here](https://stackoverflow.com/questions/46879418/spotipy-invalid-username).

For it to work you have to:

- created a Spotify application to get a client secret and id
- redirect uri Spotify application must be [the same one](https://stackoverflow.com/questions/32956443/invalid-redirect-uri-on-spotify-auth) as called in the code

# High level overview application

* get currently playing track on spotify
* get bpm of currently playing track
* move servo matching the bpm