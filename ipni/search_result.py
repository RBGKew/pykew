import requests
import time
import urllib

BASE_URL = 'http://localhost:28080/api/1'

def __url__(method, params = {}):
    return '%s/%s?%s' % (BASE_URL, method, urllib.parse.urlencode(params))

class SearchResult:
    def __init__(self, query = None):
        self.__query = query
        self.__cursor = "*"
        self.__run_query__()

    def __build__params__(self):
        params = {'perPage': 500, 'cursor': self.__cursor}
        if self.__query:
            params['q'] = self.__query
        return params

    def __run_query__(self):
        params = self.__build__params__()
        response = requests.get(__url__('search', params))
        # wait a proportion of server response time of previous call
        # before making subsequent calls
        self.__wait_time = response.elapsed.total_seconds() / 2.0
        self.__response = response.json()
        if 'results' in self.__response:
            self.__results = iter(self.__response['results'])
        if 'cursor' in self.__response:
            self.__cursor = self.__response['cursor']

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.__results)
        except StopIteration:
            time.sleep(self.__wait_time)
            self.__run_query__()
            return next(self.__results)

    def size(self):
        if 'totalResults' in self.__response:
            return self.__response['totalResults']
        else:
            return 0
