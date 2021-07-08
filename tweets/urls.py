from django.urls import path
from .views import *


urlpatterns = [
	path('', TweetListView.as_view(), name='tweet_list_view'),
	path('tweets/<int:pk>', tweet_detail_view, name='tweet_detail_view')
]