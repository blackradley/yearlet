""" Just a test """
import secrets
import tweepy

# Creating the authentication object
AUTH = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
# Setting your access token and secret
AUTH.set_access_token(secrets.access_token, secrets.access_token_secret)
# Creating the API object while passing in auth information
API = tweepy.API(AUTH)

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
PUBLIC_TWEETS = API.home_timeline()
# foreach through all tweets pulled
for tweet in PUBLIC_TWEETS:
    # printing the text stored inside the tweet object
    print tweet.text
