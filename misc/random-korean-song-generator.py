# random korean song generator by kenny zhang

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import webbrowser

scope = "user-library-read user-top-read"
# go to https://developer.spotify.com/ to grab your client_id and client_secret
client_id = ""
client_secret = ""
redirect_uri = "http://localhost:8000/callback"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

# Define a list of genres to search for
genres = ['korean','k-pop', 'korean pop', 'korean r&b', 'k-rap', 'k-idle', 'k-rnb']

# Define a list of artists to filter out
filter_artists = ['Jack Harlow', 'Bryson Tiller', 'Kairos Covers', '짱군 Zzanggoon']

# Initialize an empty list to store tracks
all_tracks = []

# Search for tracks in each genre and append them to the all_tracks list
for genre in genres:
    results = sp.search(q=f'genre:{genre}', type='track', limit=50)
    tracks = results['tracks']['items']
    tracks = [track for track in tracks if track['duration_ms'] > 60000]  # exclude tracks shorter than 1 minute
    all_tracks.extend(tracks)

# Filter out tracks with any of the specified artists
all_tracks = [track for track in all_tracks if not any(artist['name'] in filter_artists for artist in track['artists'])]

# Choose a random track from the filtered tracks
track = random.choice(all_tracks)
track_uri = track['uri']
play_link = f"spotify:track:{track_uri.split(':')[-1]}"
webbrowser.open(play_link)
