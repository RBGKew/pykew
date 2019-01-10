from .core import Api, POWO_URL, SearchResult

API = Api(POWO_URL)

def search(query, filters = None):
    return SearchResult(API, query, filters=filters)

def lookup(id, include = None):
    params = {'fields': ','.join(include)} if include else {}
    return API.get('taxon/' + id, params).json()
