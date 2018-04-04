""" Test twitter_sentiment """
from package.twitter_sentiments import TwitterSentiments
import vcr

def test_unicode_in_tweets():
    """ Err test something """
    sentiments = TwitterSentiments()
    tweets = sentiments.search("Tendring")
    first_tweet = tweets[0]
    assert "We know that one" in first_tweet.text
