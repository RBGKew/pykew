=======================================================
pykew: Python library for accessing Kew's data services
=======================================================

Library for easy access to Kew's nomenclatural and taxonomic services. Hides the
intricacies of using the HTTP API.

.. image:: https://travis-ci.com/RBGKew/pykew.svg?branch=master
    :target: https://travis-ci.com/RBGKew/pykew

.. image:: https://badge.fury.io/py/pykew.svg
    :target: https://badge.fury.io/py/pykew

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

Available Search Terms
----------------------

To build complex queries, use the search terms available in ``ipni_terms``. Query term are grouped into
the modules ``Name``, ``Author``, and ``Publication``.

``Name``
========

* added
* author
* basionym
* basionym_author
* bibliographic_reference
* citation_type
* collection_number
* collectors
* distribution
* family
* full_name
* genus
* in_powo
* infrafamily
* infragenus
* infraspecies
* modified
* name_status
* published
* published_in
* publishing_author
* rank
* scientific_name
* species
* species_author
* version

``Author``
==========

* forename
* full_name
* standard_form
* surname

``Publication``
===============

* standard_form
* bph_number
* date
* isbn
* issn
* lc_number
* preceded_by
* superceded_by
* title
* tl2_author
* tl2_number

Filtering
~~~~~~~~~

You can filter a given result set by taxonomic rank.

.. code-block:: python

    import pykew.ipni as ipni
    from pykew.ipni_terms import Filters

    res = ipni.search('Poa', filters = Filters.infraspecific)

Available Filters
-----------------

``Filters``
===========

* familial
* infrafamilial
* generic
* infrageneric
* specific
* infraspecific


Using results
~~~~~~~~~~~~~

Results sets are returned as an iterator which can be manipulated as you generally would in python. The result object
also implements ``size()`` efficiently - it does not fetch all results to count them.

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
also be retrieved.

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

Available Search Terms
----------------------

To build complex queries, use the search terms available in ``powo_terms``. Query term are grouped into
the modules ``Name``, ``Characteristic``, and ``Geography``.

``Name``
========

* full_name
* common_name
* kingdom
* family
* genus
* species
* author

``Characteristic``
==================

* summary
* appearance
* characteristic
* flower
* fruit
* leaf
* inflorescence
* seed
* cloning
* use

``Geography``
=============

* distribution

Filtering
~~~~~~~~~

You can filter a given result set by accepted taxa, taxa with images, and taxonomic rank.

.. code-block:: python

    import pykew.powo as powo
    from pykew.powo_terms import Filters

    res = powo.search('Poa', filters = [Filters.accepted, Filters.species])

Available Filters
-----------------

``Filters``
===========

* accepted
* has_images
* families
* genera
* species
* infraspecies

Individual record
~~~~~~~~~~~~~~~~~
.. code-block:: python

    import pykew.powo as powo

    res = powo.lookup('urn:lsid:ipni.org:names:320035-2')

Extra Data
----------

The standard data returned by the POWO api includes taxonomic and nomenclatural information, but there
are other data you can request.

Currently you can only retrieve distribution data, but other data should be exposed in the future.

.. code-block:: python

    import pykew.powo as powo

    res = powo.lookup('urn:lsid:ipni.org:names:320035-2', include=['distribution'])
    native_to = [d['name'] for d in res['distribution']['natives']]




Using results
~~~~~~~~~~~~~

Results sets are returned as an iterator which can be manipulated as you generally would in python. The result object
also implements ``size()`` efficiently - it does not fetch all results to count them.

.. code-block:: python

    import pykew.powo as powo
    from pykew.powo_terms import Name, Geography

    query = { Name.genus: 'Poa', Geography.distribution: 'Africa' }
    res = powo.search(query)

    res.size()
    [r['name'] for r in res if 'name' in r]
