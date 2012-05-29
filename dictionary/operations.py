from django.conf import settings
from urllib import urlencode
from urllib2 import urlopen
from dictionary.models import Entry
from django.shortcuts import get_object_or_404
import oauth2 as oauth

def send(request,entry_id):
	twitter_user = request.user.social_auth.get(provider='twitter')
	
	if not twitter_user.tokens:
	    return
	access_token = twitter_user.tokens['oauth_token']
	access_token_secret = twitter_user.tokens['oauth_token_secret']

	token = oauth.Token(access_token,access_token_secret)
	consumer_key = settings.TWITTER_CONSUMER_KEY
	consumer_secret = settings.TWITTER_CONSUMER_SECRET
	consumer = oauth.Consumer(consumer_key,consumer_secret)
	client = oauth.Client(consumer,token)

	data = (get_object_or_404(Entry, id=entry_id).content)[:115]+"..."+shorten_url("http://www.tweedictionary.com/entry/%s" %entry_id)
	request_uri = 'https://api.twitter.com/1/statuses/update.json'
	resp, content = client.request(request_uri, 'POST', urlencode(data))

def shorten_url(long_url):
     username = settings.BITLY_USERNAME
     password = settings.BITLY_PASSWORD
     bitly_url = "http://api.bit.ly/v3/shorten?login=%s&apiKey=%s&longUrl=%s&format=txt" %(username, password, long_url)
     req_url = urlencode(bitly_url)
     short_url = urlopen(req_url).read()
     return short_url
