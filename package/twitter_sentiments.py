""" Sentiment analysis test """
from __future__ import unicode_literals

from secrets import Secrets # pylint: disable=W0403
import tweepy
import textblob

class TwitterSentiments(object):
    ''' Return a list of tweets and sentiments '''
    # Language code (follows ISO 639-1 standards)
    LANGUAGE = "en"

    def __init__(self):
        pass

    def search(self, query):
        '''Search the timeline and return with sentiment rating'''
        # Creating the authentication object
        auth = tweepy.OAuthHandler(Secrets.CONSUMER_KEY, Secrets.CONSUMER_SECRET)
        # Setting your access token and secret
        auth.set_access_token(Secrets.ACCESS_TOKEN, Secrets.ACCESS_TOKEN_SECRET)
        # Creating the API object while passing in auth information
        api = tweepy.API(auth)
        # Calling the user_timeline function with our parameters
        results = api.search(q=query, lang=self.LANGUAGE)
        # foreach through all tweets pulled
        print "Here we go"
        for tweet in results:
            # printing the text stored inside the tweet object
            print tweet.text#.encode("utf-8")
            analysis = textblob.TextBlob(tweet.text)
            print analysis.sentiment.polarity
