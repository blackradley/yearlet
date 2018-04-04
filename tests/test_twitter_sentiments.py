""" Test twitter_sentiment """
from package.twitter_sentiments import TwitterSentiments
import vcr

@vcr.use_cassette('tests/vcr_cassettes/tendring_tweets.yml')
def test_first_tweet_contents():
    """ Err test something """
    sentiments = TwitterSentiments()
    tweets = sentiments.search("Tendring")
    first_tweet = tweets[0]
    assert "We all know that one" in first_tweet.text
