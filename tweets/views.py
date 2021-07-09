from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView, Response
from rest_framework.serializers import Serializer
from django.views import generic
from .models import Tweet
from .serializers import TweetsSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, 'tweets/index.html', context={})

def tweet_detail_view(request, pk, *args, **kwargs):
	return HttpResponse("this is what i think ")


class TweetHomeView(generic.View):
	template_name = 'tweets/index.html'

class TweetListView(generic.ListView):
	model = Tweet
	template_name = 'tweets/index.html'

class TweetDetailView(generic.DetailView):
	model = Tweet
	template_name = 'tweets/detail.html'


class TweetListApiView(APIView):

	def get(self, request, format=None):
		tweets = Tweet.objects.all()
		serializer = TweetsSerializer(tweets, many=True)
		return Response(serializer.data)

class TweetDetailApiView(APIView):
	
	def get(self, request, pk, format=None):
		tweet_obj = get_object_or_404(Tweet, pk=pk)
		serializer = TweetsSerializer(tweet_obj)
		return Response(serializer.data)