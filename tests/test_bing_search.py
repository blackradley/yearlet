""" Test Bing Search """
from __future__ import unicode_literals
import json
import vcr
import pytest
from src.bing_search import BingSearch

def test_method_is_present():
    """ Confirm that the method is present """
    try:
        BingSearch.search
    except AttributeError:
        pytest.fail("Method not present")

@vcr.use_cassette('tests/vcr_cassettes/bing_search_test.yml')
def test_method_returns_json():
    """ Confirm that json is returned """
    try:
        json.loads(BingSearch.search('test'))
    except ValueError:
        pytest.fail("Nope, that's not json")

