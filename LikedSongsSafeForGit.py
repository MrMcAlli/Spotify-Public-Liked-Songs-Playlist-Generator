import spotipy
from spotipy.oauth2 import SpotifyOAuth 
import spotipy.util as util


scope = 'playlist-modify-private, user-read-recently-played, playlist-modify-public, user-library-read'
user = "XXXXXX"
client_id="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
redirect_uri="https://accounts.spotify.com/api/token"



tracks = ["spotify:track:6b2oQwSGFkzsMtQruIWm2p"]
playlist_ID = "6cEzXWMWtHDyX1qnQUuvzR"

token = util.prompt_for_user_token(username=user, scope=scope,
                                    client_id=client_id,
                                    client_secret=client_secret,  
                                    redirect_uri=redirect_uri)

sp = spotipy.Spotify(auth=token)
song = ['6b2oQwSGFkzsMtQruIWm2p']

playlist = sp.user_playlist_create(user="cuzoh",name="Liked Songs")

playlist_ID = playlist["id"]

def get_playlist_tracks(username):
    results = sp.current_user_saved_tracks(limit=10)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


uTracks = get_playlist_tracks("cuzoh")

for idx, item in enumerate(uTracks):
    track = item['track']
    print(track['name'])
    if (token):
        sp.user_playlist_add_tracks(user="cuzoh", playlist_id=playlist_ID, tracks=[track['id']], position=None)


print("done")