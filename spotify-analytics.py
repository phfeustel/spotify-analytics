import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from config.spotify_client_config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, REDIRECT_URI

# To set your Spotify developer ID and secret, copy the config/spotify_client_config_example.py to config/spotify_client_config.py 
# and fill in your credentials

def client_auth():
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    ))
    return sp

def oauth_flow():
    oauth = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
    )
    sp = spotipy.Spotify(auth_manager=oauth)
    return sp

# Private playlist are only accessible through OAuth-Flow!
# See & try https://developer.spotify.com/console/get-playlist/ -> OAuth: Required
# For the OAuth flow to work the same redirect_uri needs to be set in your Spotify App -> Settings -> Redirect URIs
# When executing for the first time or with an outdated/invalid OAuth access token the command line will wait for you 
# to input the COMPLETE (redirect) URL from your browser after granting access to this app in Spotify web.
sp = oauth_flow()

# PRIVATE Playlist: wortgier + phfeustel:37i9dQZF1EJAunIyAkrpab # https://open.spotify.com/playlist/37i9dQZF1EJAunIyAkrpab?si=eeeb8862fbdf43d7
# Public: personal discover weekly: 37i9dQZEVXcUEd9E3F5ipG # https://open.spotify.com/playlist/37i9dQZEVXcUEd9E3F5ipG?si=bf5fb46544d34eae
# Public: personal stared: 7Dyr6eElhpbvG3LbUs2su3 # https://open.spotify.com/playlist/7Dyr6eElhpbvG3LbUs2su3?si=4aad9e91a44c4b5e
playlist_id='37i9dQZF1EJAunIyAkrpab'
playlist_stared_other_api = sp.playlist(playlist_id=playlist_id)
print(playlist_stared_other_api)