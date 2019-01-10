from . import ipni
from .ipni_terms import Name, Author, Publication, Filters

def test_basic_search():
    res = ipni.search('Poa Annua')
    assert res.size() == 12
    assert next(res)['id'] == '320035-2'

def test_advanced_name_search():
    query = { Name.genus: 'Poa', Name.species: 'annua', Name.author: 'L.' }
    res = ipni.search(query)
    assert res.size() == 1
    assert next(res)['id'] == '320035-2'

def test_advanced_author_search():
    res = ipni.search({Author.standard_form: 'L.'})
    assert '12653-1' in [author['id'] for author in res]

def test_advanced_publication_search():
    res = ipni.search({Publication.lc_number: 'QK91.S6'})
    assert '1071-2' in [pub['id'] for pub in res]

def test_lookup_name():
    res = ipni.lookup_name('320035-2')
    assert res['name'] == 'Poa annua'

def test_lookup_publication():
    res = ipni.lookup_publication('1071-2')
    assert res['title'] == 'Species Plantarum'

def test_lookup_author():
    res = ipni.lookup_author('12653-1')
    assert res['standardForm'] == 'L.'

def test_filter_by_family():
    q = { Name.family: 'Poaceae' }
    f = Filters.familial
    filtered = ipni.search(query = q, filters = f)

    assert filtered.size() == 1

def test_filter_by_infrafamily():
    q = { Name.family: 'Poaceae' }
    f = Filters.infrafamilial
    unfiltered = ipni.search(query = q)
    filtered = ipni.search(query = q, filters = f)

    assert filtered.size() < unfiltered.size()

def test_filter_by_generic():
    q = { Name.family: 'Poaceae' }
    f = Filters.generic
    unfiltered = ipni.search(query = q)
    filtered = ipni.search(query = q, filters = f)

    assert filtered.size() < unfiltered.size()

def test_filter_by_infrageneric():
    q = { Name.family: 'Poaceae' }
    f = Filters.infrageneric
    unfiltered = ipni.search(query = q)
    filtered = ipni.search(query = q, filters = f)

    assert filtered.size() < unfiltered.size()

def test_filter_by_specific():
    q = { Name.family: 'Poaceae' }
    f = Filters.specific
    unfiltered = ipni.search(query = q)
    filtered = ipni.search(query = q, filters = f)

    assert filtered.size() < unfiltered.size()

def test_filter_by_infraspecific():
    q = { Name.family: 'Poaceae' }
    f = Filters.infraspecific
    unfiltered = ipni.search(query = q)
    filtered = ipni.search(query = q, filters = f)

    assert filtered.size() < unfiltered.size()
