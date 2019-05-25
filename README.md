# Running the code

All codes is meant to be run using Python 3. Create a virtual environment in order to avoid having to type `python3` instead of `python` all the time. Do this using:

```
python3 -m venv venv
source venv/bin/activate
```


At the moment the only library used is `spotipy` (`gpiozero` is also used but is available in Raspbian by default) so there's not much extra use to using a virtual environment. Additional libraries would have to be added to the `requirements.txt` file.

In order not to put any credentials in the code itself there's a `config.py` file in the root folder. Fill in the following fields to set it up correctly:

```
CLIENT_ID = ''
CLIENT_SECRET = ''
USERNAME = ''
SCOPE = ''
REDIRECT_URI = ''
```

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
- copy the redirect uri manually in the browser opening

If you connect to the raspberry pi using ssh you don't have access to the browser. A workaround is to run `dancing-cat.py` on your local machine and then `scp .cache-username pi@ip` to copy the cached token to your raspberry pi.

# High level overview application

* get currently playing track on spotify
* get bpm of currently playing track
* move servo matching the bpm

# Running multiple processes at the same time

An issue arises because two things happen at the same time:

- the servo switches back and forth on the rhythm of the beat
- the bpm for each track is fetched every x seconds

It's best to keep the two separate. If this is not the case every x seconds the servo just stops working because the raspberry pi is busy fetching the updated bpm.

The issue is solved by running a program [in the background](https://raspberrypi.stackexchange.com/questions/45933/running-multiple-programs-at-once). Variables are shared between the `update-bpm` and `turn-servo` scripts by writing to the `bpm.txt` file. The complete process of opening the file, writing the bpm and closing the file again takes about 4 ms so nothing to worry about.


# to document

Make sure to install both RPi.GPIO and gpiozero on python3 (included by default in python2)
https://github.com/RPi-Distro/python-gpiozero/issues/300

```
pip install RPi.GPIO
pip install gpiozero
```