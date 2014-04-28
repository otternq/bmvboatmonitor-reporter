BMV Monitor / Serial Scripts
============================

About
------------

A python script to record data from Victron BMV-600S and BMV-602S

[![PyPi version](https://pypip.in/v/BMV/badge.png)](https://crate.io/packages/BMV/)
[![PyPi downloads](https://pypip.in/d/BMV/badge.png)](https://crate.io/packages/BMV/)

Preparations
------------

###PIP

`pip install BMV`

###Manual

```
cd /path/to/bmvmonitor
pip install -r requirements.txt
````

Tests
------------

```
cd /path/to/project/bmv
nosetests
```

###Example
```
➜  Serial scripts git:(dev_file_store) ls
CHANGES.txt      LICENSE          MANIFEST         MANIFEST.in      README.md        bin              bmv              dist             docs             requirements.txt setup.py
➜  Serial scripts git:(dev_file_store) cd bmv
➜  bmv git:(dev_file_store) ls
__init__.py           bmv.py                bmv_local_csv.pyc     bmv_local_factory.pyc bmv_local_sqlite.pyc  test
__init__.pyc          bmv_local_csv.py      bmv_local_factory.py  bmv_local_sqlite.py   bmv_remote_store.py   tests_results
➜  bmv git:(dev_file_store) nosetests
...
----------------------------------------------------------------------
Ran 3 tests in 0.586s

OK
```

Contributors
-----------

- [Nick Otter](http://github.com/otternq)
