=======================================================
pykew: Python library for accessing Kew's data services
=======================================================

----
IPNI
----

Library for searching IPNI data and looking up individual records. Hides the intracacies
of usign the HTTP API. 

Searching
---------

Simple search:

.. code-block:: python
    import pykew.ipni as ipni

    result = ipni.search('Poa annua')

Advanced search:

.. code-block:: python
    import pykew.ipni as ipni
    from pykew.ipni.terms import Name

    query = { Name.genus: 'Poa', Name.species: 'annua' }
    res = ipni.search(query)

Using results:

.. code-block:: python
    import pykew.ipni as ipni
    from pykew.ipni.terms import Name

    query = { Name.genus: 'Poa', Name.species: 'annua' }
    res = ipni.search(query)

		res.size() # 12
    [r['name'] for r in res if 'name' in r]
