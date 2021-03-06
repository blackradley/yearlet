""" Test twitter_sentiment """
from __future__ import unicode_literals
import vcr
import pytest
from src.twitter_sentiments import TwitterSentiments

def test_method_is_present():
    """ Confirm that the method is present """
    try:
        TwitterSentiments.search
    except AttributeError:
        pytest.fail("Method not present")

@vcr.use_cassette('tests/vcr_cassettes/tendring_tweets.yml')
def test_first_tweet_contents():
    """ Err test something """
    tweets = TwitterSentiments.search("Tendring")
    first_tweet = tweets[0]
    assert "We all know that one" in first_tweet.text
