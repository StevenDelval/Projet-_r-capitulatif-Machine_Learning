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
from django.views.generic import TemplateView                     
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd




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




#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
###                                                                                                                           ###
###                                                         Home                                                             ###
###                                                                                                                           ###
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################


@login_required     
def result(request):
    Track_Name = request.GET['Track_Name']  
    Artiste_Name = request.GET['Artiste_Name']  
    Genre = request.GET['Genre']  

    cid = '78e434819ce74de2a9da9bd344483f65'
    secret = '4bc5580d98ae45f087b511650c3e9d0b'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    artist_name = []
    album_name = []
    album_id = []
    track_name = []
    track_id = []
    popularity = []
    release_date = []
    duration_ms = []
    explicit = []
    external_urls = []
    is_local = []
    preview_url = []
    track_number = []
    audio_features = []
    image_url = []
    #results = sp.search(q=f'track: {Track_Name} artist:{Artiste_Name}', type='track', limit=1)

    for k,i in enumerate(range(0,50,50)):
            
                    track_results = sp.search(q=f'track: {Track_Name} artist:{Artiste_Name}', type='track', limit=13)
                    for j, t in enumerate(track_results['tracks']['items']):
                        
                        image_url.append(t['album']['images'][0]['url'])
                        # Get artist data
                        artist_name.append(t['artists'][0]['name'])
                        
                        # Get album data
                        album_name.append(t['album']['name'])
                        album_id.append(t['album']['id'])
                        release_date.append(t['album']['release_date'])
                        
                        # Get track data
                        track_name.append(t['name'])
                        track_id.append(t['id'])
                        popularity.append(t['popularity'])
                        duration_ms.append(t['duration_ms'])
                        explicit.append(t['explicit'])
                        external_urls.append(t['external_urls']['spotify'])
                        is_local.append(t['is_local'])
                        preview_url.append(t['preview_url'])
                        track_number.append(t['track_number'])
                        

                        # Get audio features
                        af = sp.audio_features(t['id'])[0]
                        audio_features.append(af)





    import pandas as pd
    track_dataframe = pd.DataFrame({
        'artist_name': artist_name,
        'album_name': album_name,
        'album_id': album_id,
        'track_name': track_name,
        'track_id': track_id,
        'popularity': popularity,
        'release_date': release_date,
        'duration_ms': duration_ms,
        'explicit': explicit,
        'external_urls': external_urls,
        'is_local': is_local,
        'preview_url': preview_url,
        'track_number': track_number,
        'audio_features': audio_features,   
        'image_url':image_url,
        })


    track_dict_list = []
    for index, row in track_dataframe.iterrows():
        track_dict_list.append(row.to_dict())

    
    if len(track_dataframe)>0:
        return render(request, 'result.html', {
            'track_dict_list': track_dict_list,
            'track_dataframe': track_dataframe,
        })
    else:
        return render(request, 'result_with_no_text.html', {
            'Track_Name': Track_Name,
            'Artiste_Name': Artiste_Name,
            'Genre':Genre,
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