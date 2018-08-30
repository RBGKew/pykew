import pykew.ipni as ipni
from pykew.ipni.terms import Name, Author, Publication

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
    assert next(res)['id'] == '12653-1'

def test_advanced_publication_search():
    res = ipni.search({Publication.lc_number: 'QK91.S6'})
    assert next(res)['id'] == '1071-2'

def test_lookup_name():
    res = ipni.lookup_name('320035-2')
    assert res['name'] == 'Poa annua'

def test_lookup_publication():
    res = ipni.lookup_publication('1071-2')
    assert res['title'] == 'Species Plantarum'

def test_lookup_author():
    res = ipni.lookup_author('12653-1')
    assert res['standardForm'] == 'L.'
