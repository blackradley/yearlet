""" Sentiment analysis test """
from __future__ import unicode_literals # all strings are unicode
# dict and str behave like python 3 using the future package
from builtins import dict, str # pylint: disable=W0622,E0401
import os
from collections import namedtuple
from dotenv import find_dotenv, load_dotenv
import tweepy
import textblob

class TwitterSentiments(object):
    ''' Return a list of tweets and sentiments '''
    # Language code (follows ISO 639-1 standards)
    LANGUAGE = "en"

    def __init__(self):
        pass

    @classmethod
    def search(cls, query):
        '''Search the timeline and return with sentiment rating'''
        load_dotenv(find_dotenv())
        # Creating the authentication object
        auth = tweepy.OAuthHandler(
            os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET")
            )
        # Setting your access token and secret
        auth.set_access_token(
            os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET")
            )
        # Creating the API object while passing in auth information
        api = tweepy.API(auth)
        # Calling the user_timeline function with our parameters
        results = api.search(q=query, lang=cls.LANGUAGE)
        # foreach through all tweets pulled
        tweets = []
        # Specify thenamedtuple.
        tweet_polarity = namedtuple('tweet_polarity', ['text', 'polarity'])
        for tweet in results:
            # printing the text stored inside the tweet object
            text = tweet.text
            analysis = textblob.TextBlob(tweet.text)
            polarity = analysis.sentiment.polarity
            tweets.append(tweet_polarity(text, polarity))
        return tweets
