#########################################################################
#                          Import packages                              #
#########################################################################

from cProfile import label
from email.mime import image
from http.client import HTTPResponse
import imp
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter                            # For scrapping twitter
import pandas as pd
import re
from stop_words import get_stop_words                                   # For cleaning text
from wordcloud import WordCloud                                         # For get a Wordcloud
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import json                                                             # For get the sentiment analysis API
import requests                                                         # For get the sentiment analysis API
import random
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect                            # For signUp page
from .forms import SignUp, UploadFileForm                               # For signUp page
from django.contrib.auth.forms import UserCreationForm                  # For signUp page methode 2
from django.urls import reverse_lazy                                    # For signUp page methode 2
from django.views import generic                                        # For signUp page methode 2
from django.views.generic import CreateView                             # For SignUp form Page  
from . import forms                                                     # For SignUp form Page 
from django.contrib.auth.decorators import login_required
import langid                                                           # For language detect
from .forms import YourTextForm                                         # For Your text analysis
from django.views.generic import TemplateView                           # For Your text analysis
from dataclasses import replace                                         # For URL text analysis
from bs4 import BeautifulSoup                                           # For URL text analysis

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
###                                                   Twitter analysis                                                        ###
###                                                                                                                           ###
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

@login_required                                     # Makes loggin mandatory
def tweet(request):
    return render(request, 'index.html')

###____________________________Scrapping____________________________###

@login_required     
def result(request):
    x = request.GET['all_words']  
    return render(request, 'result.html', {
                                            'x':x,
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