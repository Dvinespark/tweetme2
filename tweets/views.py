from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	return render(request, 'tweets/index1.html', context={})

def tweet_detail_view(request, pk, *args, **kwargs):
	print(pk, args, kwargs)
	return HttpResponse("this is what i think ")