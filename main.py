""" Sentiment Analysis Demo """
from src.twitter_sentiments import TwitterSentiments

TWEETS = TwitterSentiments.search("Tendring")
for tweet in TWEETS:
    print u"{0}".format(tweet.text).encode('utf-8', 'ignore')
