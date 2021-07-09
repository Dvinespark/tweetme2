from django.urls import path
from .views import *


urlpatterns = [

	# user application views
	path('', TweetHomeView.as_view(), name='user_tweet_home'),

	# crud operations
	path('tweets', TweetListView.as_view(), name='tweet_list_view'),
	path('tweets/<int:pk>', TweetDetailView.as_view(), name='tweet_detail_view'),
	

	# api paths
	path('api/tweets', TweetListApiView.as_view(), name='api_tweets_list'),
	path('api/tweets/<int:pk>', TweetDetailApiView.as_view(), name='api_tweets_detail'),
]