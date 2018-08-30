import requests
import time
import urllib

from .config import BASE_URL

def _url(method, params = {}):
    return '{base}/{method}?{opt}'.format(base=BASE_URL, method=method, opt=urllib.parse.urlencode(params))

class SearchResult:
    def __init__(self, query = None):
        self._query = query
        self._cursor = "*"
        self._run_query()

    def _build_params(self):
        params = {'perPage': 500, 'cursor': self._cursor}
        if self._query:
            params['q'] = self._format_query()
        return params

    def _format_query(self):
        if isinstance(self._query, dict):
            terms = [k.value + ':' + v for k, v in self._query.items()]
            return ",".join(terms)
        else:
            return self._query

    def _run_query(self):
        params = self._build_params()
        response = requests.get(_url('search', params))
        # wait a proportion of server response time of previous call
        # before making subsequent calls
        self._wait_time = response.elapsed.total_seconds() / 2.0
        self._response = response.json()
        if 'results' in self._response:
            self._results = iter(self._response['results'])
        if 'cursor' in self._response:
            self._cursor = self._response['cursor']

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._results)
        except StopIteration:
            time.sleep(self._wait_time)
            self._run_query()
            return next(self._results)

    def size(self):
        if 'totalResults' in self._response:
            return self._response['totalResults']
        else:
            return 0
