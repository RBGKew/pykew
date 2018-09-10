=======================================================
pykew: Python library for accessing Kew's data services
=======================================================

Library for easy access to Kew's nomenclatural and taxonomic services. Hides the
intracacies of usign the HTTP API. 

----
IPNI
----

Module for searching IPNI data and looking up individual records. 

Simple search
~~~~~~~~~~~~~

.. code-block:: python

    import pykew.ipni as ipni

    result = ipni.search('Poa annua')

Advanced search
~~~~~~~~~~~~~~~

.. code-block:: python

    import pykew.ipni as ipni
    from pykew.ipni_terms import Name

    query = { Name.genus: 'Poa', Name.species: 'annua' }
    res = ipni.search(query)

Using results
~~~~~~~~~~~~~

.. code-block:: python

    import pykew.ipni as ipni
    from pykew.ipni_terms import Name

    query = { Name.genus: 'Poa', Name.species: 'annua' }
    res = ipni.search(query)
    
    res.size()
    [r['name'] for r in res if 'name' in r]

----
POWO
----

Module for searching POWO data and looking up individual records. Taxonomic data is
returned by default, but other associated such as distributions and descriptive text can
also be retreived.

Simple search
~~~~~~~~~~~~~

.. code-block:: python

    import pykew.powo as powo

    result = powo.search('Poa annua')

Advanced search
~~~~~~~~~~~~~~~

.. code-block:: python

    import pykew.powo as powo
    from pykew.powo_terms import Name

    query = { Name.genus: 'Poa', Name.species: 'annua' }
    res = powo.search(query)

Individual record
~~~~~~~~~~~~~~~~~
.. code-block:: python

    import pykew.powo as powo

    res = powo.lookup('urn:lsid:ipni.org:names:320035-2', include=['distribution'])
    native_to = [d['name'] for d in res['distribution']['natives']]

Using results
~~~~~~~~~~~~~

.. code-block:: python

    import pykew.powo as powo
    from pykew.powo_terms import Name, Geography

    query = { Name.genus: 'Poa', Geography.distribution: 'Africa' }
    res = powo.search(query)
    
    res.size()
    [r['name'] for r in res if 'name' in r]
