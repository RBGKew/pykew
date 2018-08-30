import ipni

def test_ipni():
    res = ipni.search('Aa')
    assert res.size() == 57
    assert next(res)
