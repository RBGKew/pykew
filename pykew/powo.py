from .core import Api, POWO_URL, SearchResult

API = Api(POWO_URL)

def search(query = None):
    return SearchResult(API, query=query)

def lookup_name(id):
    return API.get('taxon/' + id).json()
