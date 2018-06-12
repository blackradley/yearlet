""" Sentiment analysis test """
from __future__ import unicode_literals # all strings are unicode
# dict and str behave like python 3 using the future package
from builtins import dict, str # pylint: disable=W0622,E0401
import os
import requests
from dotenv import find_dotenv, load_dotenv

class BingSearch(object):
    ''' Use the Bing search API '''
    # Language code (follows ISO 639-1 standards)
    LANGUAGE = "en"
    SEARCH_URL = "https://api.cognitive.microsoft.com/bing/v7.0/search"

    def __init__(self):
        pass

    @classmethod
    def search(cls, query):
        """ Search Bing and return json """
        # only 3 calls per second and 3000 per month on the free tier
        load_dotenv(find_dotenv())
        headers = {'Ocp-Apim-Subscription-Key': os.getenv("BING_SEARCH_KEY")}
        params = {"q": query}
        response = requests.get(cls.SEARCH_URL, headers=headers, params=params)
        response.raise_for_status() # raise an exception if it doesn't work
        return response.content
