cookiecutter-urga-djcms
=======================


A cookiecutter_ template for Django.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Aims - should become 'features'
-------------------------------

* For Django 1.8
* Based on django-cms_ 3.1
* Renders Django projects with 100% test coverage
* Twitter Bootstrap_ v4.0.0 - alpha_
* Mandrill_ for sending mail
* 12-Factor_ based settings via local .env file
* Gulp build for generating css (using libsass) and optimize images
* Media storage using Amazon S3/Google Storage
* Serve static files Whitenoise_
* Docker support using docker-compose_ for dev and prod

.. _django-cms: http://www.django-cms.org/en/
.. _alpha: http://blog.getbootstrap.com/2015/08/19/bootstrap-4-alpha/
.. _Bootstrap: https://github.com/twbs/bootstrap
.. _Mandrill: http://www.mandrillapp.com
.. _12-Factor: http://12factor.net/
.. _Whitenoise: https://whitenoise.readthedocs.org/
.. _docker-compose: https://www.github.com/docker/compose


Constraints
-----------

* Only maintained 3rd party libraries are used.
* PostgreSQL everywhere (9.0+)
* Environment variables for configuration (This won't work with Apache/mod_wsgi).


Usage
------

Let's pretend you want to create a Django-cms website called "b2bmarketing". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/urga/cookiecutter-urga-djcms

You'll be prompted for some questions, answer them, then it will create a Django-cms project for you.

**Warning**: After this point, change 'Urga', 'Urga Creative Commumication', etc to your own information.

It prompts you for questions. Answer them::

    Cloning into 'cookiecutter-urga-djcms'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [project_name]: b2b marketing
    repo_name [Reddit_Clone]: b2bmarketing
    author_name [Your Name]: Urga Creatieve Communicatie
    email [Your email]: info@urga.be
    description [A short description of the project.]: A self-maintainable b2b marketing website.
    domain_name [example.com]: b2bmarketing.com
    version [0.0.1]: 0.0.1
    timezone [CET]:
    now [2015/01/13]: 2015/08/30
    year [2015]:


Enter the project and take a look around::

    $ cd b2bmarketing/
    $ ls

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:urga/b2bmarketing.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?


Getting up and running using docker
-----------------------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* docker
* docker-compose

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f dev.yml up

You can also set the environment variable ``COMPOSE_FILE`` pointing to ``dev.yml`` like this::

    $ export COMPOSE_FILE=dev.yml

And then run::

    $ docker-compose up


To migrate your app and to create a superuser, run::

    $ docker-compose run django python manage.py migrate

    $ docker-compose run django python manage.py createsuperuser

**Gulp tasks**

YET TO BE WRITTEN


"Your Stuff"
-------------

Scattered throughout the Python and HTML of this project are places marked with "your stuff". This is where third-party libraries are to be integrated with your project.


Not Exactly What You Want?
---------------------------

This is what I want. *It might not be what you want.* Don't worry, you have options:

Fork This
~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this to create your own version.
Once you have your fork working, let me know and I'll add it to a '*Similar Cookiecutter Templates*' list here.
It's up to you whether or not to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

* cookiecutter_ so it gets listed in the README as a template.
* The cookiecutter grid_ on Django Packages.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _grid: https://www.djangopackages.com/grids/g/cookiecutters/

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they make my own project development
experience better.
