Python Test Assignment
====================================

Requirements
============
* Python 3.6 >=
* Django 3.0.2
* PostgreSQL 10.10

mkvirtualenv testapp --python=/usr/bin/python3.6

Create settings_local.py at directory settings and override DB settings
example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'admin',
        'PASSWORD': '111111',
        'HOST': 'localhost',
        'PORT': 5432,
        'NAME': 'categories',
    }
}

```

Create DB (fox Linux):
======================
- psql
```sql
CREATE DATABASE categories;
```

Update or install packages
================================
pip install -U -r .meta/packages


Apply migrations:
==================
./manage.py migrate


Development
============
./manage.py runserver


Install packages for tests
===================================
pip install -r .meta/packages.tests

Run tests
========================
./manage.py test

Flake8
========================
flake8 --ignore=E501 --exclude=settings --show-source --statistics --count .
