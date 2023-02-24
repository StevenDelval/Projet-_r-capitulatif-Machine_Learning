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
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


    results = sp.search(q=f'track: {Track_Name} artist:{Artiste_Name}', type='track', limit=1)

    # Iterate over the search results and append the track names to the list


    return render(request, 'result.html', {
                                            'popularity':results['tracks']['items'][0]['popularity'],
                                            }
                                            )

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