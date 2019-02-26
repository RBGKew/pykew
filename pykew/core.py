import requests
import time
import urllib

IPNI_URL = 'http://beta.ipni.org/api/1'
POWO_URL = 'http://www.plantsoftheworldonline.org/api/2'
KPL_URL = 'http://kewplantlist.org/api/v1'

class Api:
    def __init__(self, url):
        self._base_url = url

    def _url(self, method, params):
        return '{base}/{method}?{opt}'.format(
                base=self._base_url,
                method=method,
                opt=urllib.parse.urlencode(params))

    def get(self, method, params = {}):
        resp = requests.get(self._url(method, params))
        if resp.status_code == 249: # too many requests, retry after 5 sec
            time.sleep(5)
            return self.get(method, params)
        return resp

class SearchResult:
    def __init__(self, api, query, filters = None):
        self._query = query
        self._filters = filters
        self._api = api
        self._cursor = "*"
        self._run_query()

    def _build_params(self):
        params = {'perPage': 500, 'cursor': self._cursor}
        if self._query:
            params['q'] = self._format_query()
        if self._filters:
            params['f'] = self._format_filters()
        return params

    def _format_query(self):
        if isinstance(self._query, dict):
            terms = [k.value + ':' + v for k, v in self._query.items()]
            return ",".join(terms)
        else:
            return self._query

    def _format_filters(self):
        if isinstance(self._filters, list):
            terms = [f.value for f in self._filters]
            return ",".join(terms)
        else:
            return self._filters.value

    def _run_query(self):
        params = self._build_params()
        response = self._api.get('search', params)
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
