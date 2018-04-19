""" Sentiment Analysis Demo """
from package.secrets import Secrets

SENTIMENTS = TwitterSentiments()
TWEETS = SENTIMENTS.search("Tendring")
for tweet in TWEETS:
    print u"{0}".format(tweet.text).encode('utf-8', 'ignore')
