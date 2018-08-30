import requests

from .search_result import SearchResult
from .search_result import __url__

def search(query = None):
    return SearchResult(query)

def lookup_name(id):
    return requests.get(__url__('n/%s' % id)).json()

def lookup_author(id):
    return requests.get(__url__('a/%s' % id)).json()

def lookup_publication(id):
    return requests.get(__url__('p/%s' % id)).json()
