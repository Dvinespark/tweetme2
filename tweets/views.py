from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, 'tweets/index1.html', context={})

def tweet_detail_view(request, pk, *args, **kwargs):
	return HttpResponse("this is what i think ")


class TweetListView(generic.ListView):
	model = Tweet
	template_name = 'tweets/index.html'