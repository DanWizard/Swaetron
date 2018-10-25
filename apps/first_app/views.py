from django.shortcuts import render, redirect
from .models import *
import re 
import tweepy 
from tweepy import OAuthHandler 
from datetime import datetime

consumer_key = 'sRgDsLD2ooisushlfKkHZSDAx'
consumer_secret = 'NEj3dIxggttoGsLA3qoPX6rw02wMt0z0aGfjjAQ5I2E99aYBke'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def renderHome(request):
	return render(request,'first_app/home.html')

def renderDates(request):
	data = []
	hold = {
	'Location':None,
	'Photo':None,
	'Time':None,
	'Date':None,
	}
	superquery = api.user_timeline('sweatpolo', count = 200)
	check_title = re.compile('[a-zA-Z]+')
	check_if_time = re.compile('[0-1]?[0-9]:[0-5][0-9]([ ]*[p|a][.][m][.])?')
	check_if_date = re.compile('[0-1][0-9]/[0-3][0-9]/\d{4}')
	now = datetime.now()

	for i in range(0,len(superquery)):
		try:
			exist = check_if_date.search(superquery[i].text)
			passed_date = check_if_date.search(superquery[i].text)[0]
			event_date = datetime.strptime(passed_date, '%m/%d/%Y')
		except Exception as e:
			event_date = datetime.strptime('01/01/1000', '%m/%d/%Y')
			print(e)

		if 'media' in superquery[i].entities and superquery[i].retweeted == False and event_date > now and exist:
			
			try:
				hold['Location'] = superquery[i].entities['urls'][0]['expanded_url']
			except Exception as e:
				hold['Location'] = None
			try:
				hold['Time'] = check_if_time.search(superquery[i].text)[0]
			except Exception as e:
				hold['Time'] = None
			try:
				hold['Date'] = passed_date
			except Exception as e:
				hold['Date'] = None

			hold['Photo'] = superquery[i].entities['media'][0]['media_url_https']
			data.append(hold)
			hold = {}

	content = {
	'data': data
	,
	}

	print(content)
	return render(request,'first_app/Dates.html', content)

def renderShop(request):
	return render(request,'first_app/Shop.html')

def renderMusic(request):
	return render(request,'first_app/Music.html')

def processEmail(request):
	results = User.objects.checkEmail(request.POST)
	if "incorrect" in results:
		for key, value in results.items():
	 		messages.error(request, value)
	else:
		User.objects.create(email=request.POST['email'])
		for key, value in results.items():
			messages.error(request,value)
	return redirect('/')

def processEmail_shop(request):
	results = User.objects.checkEmail(request.POST)
	if "incorrect" in results:
		for key, value in results.items():
	 		messages.error(request, value)
	else:
		User.objects.create(email=request.POST['email'])
		for key, value in results.items():
			messages.error(request,value)
	return redirect('/shop')




