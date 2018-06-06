""" Test twitter_sentiment """
from src.twitter_sentiments import TwitterSentiments
import vcr

@vcr.use_cassette('tests/vcr_cassettes/tendring_tweets.yml')
def test_first_tweet_contents():
    """ Err test something """
    tweets = TwitterSentiments.search("Tendring")
    first_tweet = tweets[0]
    assert "We all know that one" in first_tweet.text
