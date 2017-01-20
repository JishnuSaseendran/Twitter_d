from django.shortcuts import render
from django.views.generic import View
from tweet.tweetpy import tweets
import json

def home(request):
    return render(request, 'index.html')
def results(request):
    t=None
    twit_id=request.POST.get(str('id_twitter'))
    t=tweets(twit_id)
    return render(request, 'results.html',{'datas':t, 'twit_id':twit_id})

