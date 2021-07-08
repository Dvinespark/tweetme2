from django.urls import path
from .views import home_view, tweet_detail_view


urlpatterns = [
	path('<int:pk>', home_view, name='home_view'),
	path('tweets/<int:pk>', tweet_detail_view, name='tweet_detail_view')
]