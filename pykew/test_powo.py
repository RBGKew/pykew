from . import powo
from .powo_terms import Name, Characteristic, Geography, Filters

def test_basic_search():
    res = powo.search('Poa Annua')
    assert res.size() >= 2
    assert next(res)['fqId'] == 'urn:lsid:ipni.org:names:320035-2'

def test_advanced_name_search():
    query = { Name.genus: 'Poa', Name.species: 'annua', Name.author: 'L.' }
    res = powo.search(query)
    assert res.size() == 1
    assert next(res)['fqId'] == 'urn:lsid:ipni.org:names:320035-2'

def test_advanced_characteristic_search():
    query = { Characteristic.flower: 'yellow', Characteristic.leaf: 'alternate' }
    res = powo.search(query)
    assert res.size() > 0

def test_advanced_geography_search():
    res = powo.search({Geography.distribution: 'Africa'})
    assert res.size() > 0

def test_lookup():
    res = powo.lookup('urn:lsid:ipni.org:names:320035-2')
    assert res['name'] == 'Poa annua'

def test_lookup_with_extra_fields():
    res = powo.lookup('urn:lsid:ipni.org:names:320035-2', include=['distribution', 'descriptions'])
    assert 'distribution' in res
    assert 'descriptions' in res

def test_filters():
    q = { Name.family: 'Poaceae' }
    f = Filters.accepted
    unfiltered = powo.search(q)
    filtered = powo.search(q, filters = f)

    assert filtered.size() < unfiltered.size()
