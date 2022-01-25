import pykew.core
from .core import Api, POWO_URL, SearchResult
from typing import List


API = Api(POWO_URL)

def search_all_pages(query, filters=None)->List[pykew.core.SearchResult]:
    first_page = SearchResult(API, query, filters=filters,page_number=0)
    num_pages = first_page._response['totalPages']

    all_results = [first_page]
    if num_pages>1:
        for i in range(1,num_pages):

            all_results.append(SearchResult(API, query, filters=filters,page_number=i))

    return all_results

def search(query, filters = None,page_number=0):
    return SearchResult(API, query, filters=filters,page_number=page_number)

def lookup(id, include = None):
    params = {'fields': ','.join(include)} if include else {}
    return API.get('taxon/' + id, params).json()
