from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
# Create your views here.
import tweepy
import os

consumer_key = os.environ["Twitter_Api"]
consumer_secret = os.environ["Twitter_Api_secret"]
access_token = os.environ["Twitter_access"]
access_token_secret = os.environ["Twitter_access_secret"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



def hello(request):
    value = False
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            try:
                if username[0]=='@':
                    username = username[1:]
                api.update_status(f"@{username} *slap*")
                print(f"{username} slap sent and done")
            except:
                print("Not Done")
            value = True
    else:
        form = NameForm()
    return render(request,'bonk/index.html',{'form':form,'value':value})