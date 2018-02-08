""" Just a test """
import secrets
import tweepy

# Creating the authentication object
AUTH = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
# Setting your access token and secret
AUTH.set_access_token(secrets.access_token, secrets.access_token_secret)
# Creating the API object while passing in auth information
API = tweepy.API(AUTH)

# The search term you want to find
query = "West Midlands"
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
results = API.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print tweet.user.screen_name,"Tweeted:",tweet.text
