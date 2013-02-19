==========
nose-watch
==========

.. image:: https://secure.travis-ci.org/lukaszb/nose-watch.png?branch=master
  :target: http://travis-ci.org/lukaszb/nose-watch

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

To test the package you can simply run::

    nosetests

.. note:: Please do not use the plugin itself (--with-watch) to test the plugin
   as it would be picked by nose before the one from repository. If you want to
   watch for changes please use provided ``watch-tests.sh`` script.

.. _watchdog: http://pypi.python.org/pypi/watchdog
.. _tox: http://pypi.python.org/pypi/tox

