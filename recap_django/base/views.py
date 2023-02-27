#########################################################################
#                          Import packages                              #
#########################################################################

from django.http import HttpResponseRedirect                            # For signUp page
from .forms import SignUp, UploadFileForm                               # For signUp page
from django.contrib.auth.forms import UserCreationForm                  # For signUp page methode 2
from django.urls import reverse_lazy                                    # For signUp page methode 2
from django.views import generic                                        # For signUp page methode 2
from django.views.generic import CreateView                             # For SignUp form Page  
from . import forms                                                     # For SignUp form Page 
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView                           # For Your text analysis
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


                                          # For URL text analysis

#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
###                                                                                                                           ###
###                                                         About                                                             ###
###                                                                                                                           ###
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

def about(request):
    return render(request, 'about.html')



###____________________________Scrapping____________________________###

@login_required     
def result(request):
    Track_Name = request.GET['Track_Name']  
    Artiste_Name = request.GET['Artiste_Name']  

    cid = '78e434819ce74de2a9da9bd344483f65'
    secret = '4bc5580d98ae45f087b511650c3e9d0b'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q=f'track: {Track_Name} artist:{Artiste_Name}', type='track', limit=1)

    # Extract additional information from the search results
    for j, t in enumerate(results['tracks']['items']):
    # Get artist data
        artist_name = t['artists'][0]['name']

        # Get album data
        album_name = t['album']['name']
        album_id = t['album']['id']
        release_date = t['album']['release_date']

        # Get track data
        track_name = t['name']
        track_id = t['id']
        popularity = t['popularity']
        duration_ms = t['duration_ms']
        explicit = t['explicit']
        external_urls = t['external_urls']['spotify']
        is_local = t['is_local']
        preview_url = t['preview_url']
        track_number = t['track_number']

        # Get audio features
        af = sp.audio_features(t['id'])[0]
        danceability = af['danceability']
        energy = af['energy']
        key = af['key']
        loudness = af['loudness']
        mode = af['mode']
        speechiness = af['speechiness']
        acousticness = af['acousticness']
        instrumentalness = af['instrumentalness']
        liveness = af['liveness']
        valence = af['valence']
        tempo = af['tempo']
        duration_ms = af['duration_ms']
        time_signature = af['time_signature']


    

    return render(request, 'result.html', {
        'artist_name': artist_name,
        'album_name': album_name,
        'album_id': album_id,
        'release_date': release_date,
        'track_name': track_name,
        'track_id': track_id,
        'popularity': popularity,
        'duration_ms': duration_ms,
        'explicit': explicit,
        'external_urls': external_urls,
        'is_local': is_local,
        'preview_url': preview_url,
        'track_number': track_number,
        'danceability': danceability,
        'energy': energy,
        'key': key,
        'loudness': loudness,
        'mode': mode,
        'speechiness': speechiness,
        'acousticness': acousticness,
        'instrumentalness': instrumentalness,
        'liveness': liveness,
        'valence': valence,
        'tempo': tempo,
        'time_signature': time_signature,
    })

def home(request):
    return render(request, 'home.html')



#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
###                                                                                                                           ###
###                                                     SignUp form Page                                                      ###
###                                                                                                                           ###
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

class SignupPage(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = './registration/signup.html'