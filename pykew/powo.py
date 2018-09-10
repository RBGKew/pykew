from .core import Api, POWO_URL, SearchResult

API = Api(POWO_URL)

def search(query = None):
    return SearchResult(API, query=query)

def lookup(id, include = None):
    params = {'fields': ','.join(include)} if include else {}
    return API.get('taxon/' + id, params).json()
