from .core import Api, IPNI_URL, SearchResult

API = Api(IPNI_URL)

def search(query, filters = None):
    return SearchResult(API, query, filters=filters)

def lookup_name(id):
    return API.get('n/' + id).json()

def lookup_author(id):
    return API.get('a/' + id).json()

def lookup_publication(id):
    return API.get('p/' + id).json()
