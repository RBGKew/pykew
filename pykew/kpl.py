from .core import Api, KPL_URL, SearchResult

API = Api(KPL_URL)

def search(query = None):
    return SearchResult(API, query=query)

def lookup(id, include = None):
    return API.get('taxon/' + id).json()
