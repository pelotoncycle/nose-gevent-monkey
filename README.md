nose-gevent-monkey
==================

A nose plugin for monkey patching modules for use with gevent.

Installation
------------

```bash
$ pip install nose-gevent-monkey
```

Usage
-----

Monkey patch the default modules patched by `gevent.monkey.patch_all()`.

```
$ nosetests --with-geventmonkey --gevent-monkey-patch-all
```

Monkey patch the default modules patched by `gevent.monkey.patch_all()` plus
`subprocess`.

```
$ nosetests --with-geventmonkey --gevent-monkey-patch-all --gevent-monkey-patch subprocess
```

Monkey patch the default modules patched by `gevent.monkey.patch_all()` minus
`time`.

```
$ nosetests --with-geventmonkey --gevent-monkey-patch-all --gevent-monkey-no-patch time
```

Monkey patch just `threading` and `os`.

```
$ nosetests --with-geventmonkey --gevent-monkey-patch threading,os
```
