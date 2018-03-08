""" Sentiment analysis test """
from __future__ import unicode_literals

from package.twitter_sentiments import TwitterSentiments

SENTIMENTS = TwitterSentiments()
SENTIMENTS.search("Tendring")
