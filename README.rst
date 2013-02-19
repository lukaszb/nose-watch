==========
nose-watch
==========

A Nose plugin that allows to run tests continuously (uses watchdog_ for
listening to filesystem events).


Installation
============

Usual thing:

    pip install nose-watch


How to use
==========

In order to use this plugin use the ``--with-watch`` switch::

    nosetests --with-watch

You can pass any other options/arguments, tests should be run normally but
process would stay there and watch for changes on ``*.py`` files. Every change
should re-run tests.


Development
===========

We use tox_ for tests. Repository is at https://github.com/lukaszb/nose-watch/.
We prefer pull requests for sending patches.

.. _watchdog: http://pypi.python.org/pypi/watchdog
.. _tox: http://pypi.python.org/pypi/tox

