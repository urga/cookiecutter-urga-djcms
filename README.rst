cookiecutter-urga-djcms
=======================


A cookiecutter_ template for Django.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Aims - should become 'features'
-------------------------------

* For Django 1.8
* Based on django-cms_ 3.1
* Renders Django projects with 100% test coverage
* Minimal responsive css
* Mandrill_ for sending mail
* 12-Factor_ based settings via local .env file
* Gulp build for generating css (using libsass) and optimize images
* Bower
* Media storage using Amazon S3/Google Storage
* Docker

.. _django-cms: http://www.django-cms.org/en/
.. _Mandrill: http://www.mandrillapp.com
.. _12-Factor: http://12factor.net/


Constraints
-----------

* Only maintained 3rd party libraries are used.
* PostgreSQL everywhere (9.0+)
* Environment variables for configuration (This won't work with Apache/mod_wsgi).


Usage
------

First, get cookiecutter::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/urga/cookiecutter-urga-djcms

You'll be prompted for some questions, answer them, then it will create a Django-cms project for you.

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:urga/b2bmarketing.git
    $ git push -u origin master


Getting up and running using docker
-----------------------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* docker
* docker-compose

Open a terminal at the project root and run the following for local development::

    $ docker-compose up


To migrate your app and to create a superuser, run::

    $ docker-compose run django python manage.py migrate

    $ docker-compose run django python manage.py createsuperuser

**Gulp tasks**

YET TO BE WRITTEN
