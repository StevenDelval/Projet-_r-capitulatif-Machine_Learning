
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '78e434819ce74de2a9da9bd344483f65'
secret = '4bc5580d98ae45f087b511650c3e9d0b'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

Track_Name = "Black Summer"
Artiste_Name = "Red Hot Chili Peppers"
results = sp.search(q=f'track: {Track_Name} artist:{Artiste_Name}', type='track', limit=1)



print(results['tracks']['items'][0]['popularity'])