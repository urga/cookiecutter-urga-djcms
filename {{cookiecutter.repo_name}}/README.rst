==========
Installing
==========

1. Cloning the repo
-------------------

::

   mkdir {{ cookiecutter.repo_name }}
   cd {{ cookiecutter.repo_name }}
   git clone git@gitlab.com:urga/{{ cookiecutter.repo_name }}.git .

2. Create a virtual environment
-------------------------------

We recommend using virtualenvwrapper, which is a tiny wrapper around virtualenv that keeps all environments in one place and adds some convenient command line shortcuts. Read up on it `here <https://virtualenvwrapper.readthedocs.org/en/latest/>`_.

::

    mkvirtualenv {{ cookiecutter.repo_name }}
    setvirtualenvproject

Your shell prompt should update and tell you what environment your in: ``({{ cookiecutter.repo_name }})``.
The ``setvirtualenvproject`` command allows us to easily jump back to the project directory from wherever we are with the ``cdproject`` command.

You can switch virtualenvironments simply by typing ``workon [myenv]``. You get out of an active environment by typing ``deactivate``. Simple.

3. Install the requirements
---------------------------
::

    pip install -r requirements/local.txt

4. Install Gulp
----------------
Gulp is used for preprocessing the less files and minifies them so they are nice and tidy. It's a node package, so you need to have npm installed on your system already. Then, from the project root directory run:

::

    npm install

This will install ``gulp`` and its dependancies. If you want to add gulp packages, don't forget to specify them in the package.json file.

5. Start the watcher for generating css on the fly
--------------------------------------------------

::

    gulp watch

Use another terminal window for this. If you do that, don't forget to switch to the right environment: ``workon {{ cookiecutter.repo_name }}``.

6. Configure your environment
-----------------------------
Django needs a secret key to run. That key is not stored in the repo for security reasons, so you should generate it for every installation and save it to the environment that is read in when using Django management command.
The default is not to run in DEBUG mode, unless the environment specifies it.
The database settings are also saved in the environment and parsed using dj_database_url to map them to something Django can understand.
Because we also want to make use of Django's protection mechanism, whe also have to define hosts that are allowed to access our app.
::

    echo DJANGO_SECRET_KEY=`./secret_key_gen.py`>.env
    echo DJANGO_DEBUG=1>>.env
    echo DATABASE_URL=postgres://postgres@localhost/{{ cookiecutter.repo_name }}>>.env
    echo DJANGO_ALLOWED_HOSTS=127.0.0.1>>.env


7. Sync the database
--------------------
Create the database if it doesn't exist and sync it.
::

    createdb {{ cookiecutter.repo_name }}
    ./manage.py syncdb && ./manage.py migrate

8. Run the project
------------------
::

    ./manage.py runserver


Load/dump data from the database
--------------------------------

export:
::

    pg_dump {{ cookiecutter.repo_name }} > {{ cookiecutter.repo_name }}-`date +\%Y\%m\%d-\%Hh\%M`.sql

import:
::

    psql {{ cookiecutter.repo_name }} < {{ cookiecutter.repo_name }}-whatever.sql

Adjusting the environment
-------------------------

This project uses dotenv, a python package that reads in the ``.env`` file in the root directory. A lot of project settings depend on it and we believe in the methodology suggesting by 12factor to keep host dependant configuration out of source control. Read more on http://12factor.net/config. If you want to add or change some settings, simply edit the ``.env`` file. You can comment out lines to deactivate the setting as well.

Adding a front-end package
--------------------------

This project uses django-bower, a thin wrapper around Bower that lets you specify front-end packages in Django settings. Bower is a simple package manager for front-end stuff, e.g.: if you want to use bootstrap simply run ``bower install bootstrap``. You can specify specific versions and also dependancies. Beware, bower needs to be installed at system level, not project level. So if you haven't got it yet, run:
::

    npm install -g bower

Once that is done, you can install new packages like so:

::

    ./manage.py install bootstrap

Check out the bower website: http://bower.io/
