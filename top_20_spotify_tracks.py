# top_20_spotify_tracks by kenny zhang
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read user-top-read"
# go to https://developer.spotify.com/ to grab your client_id and client_secret
client_id = ""
client_secret = ""
redirect_uri = "http://localhost:8000/callback"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

top_tracks = sp.current_user_top_tracks(limit=20, time_range='short_term')
for i, item in enumerate(top_tracks['items']):
    artists = ", ".join([artist['name'] for artist in item['artists']])
    print(f"{i+1}. {item['name']} by {artists}")
print("\n")
