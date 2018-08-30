import requests

from .search_result import SearchResult
from .search_result import _url

def search(query = None):
    return SearchResult(query)

def lookup_name(id):
    return requests.get(_url('n/' + id)).json()

def lookup_author(id):
    return requests.get(_url('a/' + id)).json()

def lookup_publication(id):
    return requests.get(_url('p/' + id)).json()
