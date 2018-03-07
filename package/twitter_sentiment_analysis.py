""" Sentiment analysis test """
from __future__ import unicode_literals # All strings are unicode
#from builtins import dict, str
import secrets
import tweepy
import textblob

# Creating the authentication object
AUTH = tweepy.OAuthHandler(secrets.CONSUMER_KEY, secrets.CONSUMER_SECRET)
# Setting your access token and secret
AUTH.set_access_token(secrets.ACCESS_TOKEN, secrets.ACCESS_TOKEN_SECRET)
# Creating the API object while passing in auth information
API = tweepy.API(AUTH)

# The search term you want to find
QUERY = "Tendring"
# Language code (follows ISO 639-1 standards)
LANGUAGE = "en"

# Calling the user_timeline function with our parameters
RESULTS = API.search(q=QUERY, lang=LANGUAGE)

# foreach through all tweets pulled
print "Here we go"
for tweet in RESULTS:
    # printing the text stored inside the tweet object
    print tweet.text#.encode("utf-8")
    analysis = textblob.TextBlob(tweet.text)
    print analysis.sentiment.polarity
