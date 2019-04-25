# Releasing to PyPi

PyPi releases are automated via travis-ci. To push out a new version update the version
number in `pykew/__version__.py` and tag the commit with the same version number. For
example, in `__version__.py` set `VERSION = (0, 1, 3)` then run

    git commit -a -m 'Bump version to 0.1.3'
    git tag v0.1.3
    git push
    git push --tags

This will trigger a travis build and upload to pypi. If you do not tag the commit,
travis will run tests but will not push anything to pypi.
