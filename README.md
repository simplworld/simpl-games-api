# SIMPL Games Framework API Project

This project uses Python 3.5.x and Django 1.9.x

## Getting Started

### To setup python-dev Vagrant box with PostgreSQL

```bash
$ git clone ssh://git@stash.wharton.upenn.edu:7999/vagrant/python-dev-centos7.git
$ cd python-dev-centos7
$ vagrant up
$ vagrant ssh
$ cd /vagrant/examples/
$ sudo ./install_postgres.sh
```

### Setup simpl-games-api (assumes working in python-dev-centos7 vagrant)

```bash
vagrant ssh
cd /vagrant/html
git clone git@learninglab.githost.io:lldev-team/simpl-games-api.git

$ mkvirtualenv simpl-games-api
$ add2virtualenv /vagrant/html/simpl-games-api
```

### Python Setup (assumes working in python-dev-centos7 vagrant)

```bash
$ cd /vagrant/html/simpl-games-api
$ pip install -r requirements.txt
```

### Create PostgreSQL database

Create a database (defaults to Postgres):

```bash
$ createdb simpl
```

### Database Setup

Sync models to database:

```bash
$ ./manage.py migrate
```

### Create a superuser for testing

Create a superuser account to access the admin:

```bash
$ ./manage.py createsuperuser
```

For local development, run:

```bash
$ ./manage.py create_vagrant_user
```

This creates a super user with id 'vagrant@wharton.upenn.edu' and password 'vagrant' and ensures test users can be assigned passwords in scripts.

### Settings setup

Setup the `DJANGO_SETTINGS_MODULE` to use:

```bash
$ export DJANGO_SETTINGS_MODULE=config.settings.local
```

### Start the web server

```bash
$ ./manage.py runserver 0.0.0.0:8100
```

### Run tests

Install the test requirements in your virtualenv:

```bash
$ pip install -r requirements.txt
```

Then run `py.test`:

```bash
$ export DJANGO_SETTINGS_MODULE=config.settings.test
$ py.test
```

Do not commit code if tests are failing.

## Release

To release a new version of the docker image, tag a new version with `bumpversion`:

```
$ bumpversion patch
```

Then push to the repo:

```
$ git push && git push --tags
```


## Generate updated ERD of Models

```bash
$ ./manage.py graph_models games -o docs/models.png
```

## What's where?

- [API Docs](http://localhost:8100/docs/)
- The [SIMPL api](http://localhost:8100/apis/)
- [Django Admin](http://localhost:8100/admin/)
- [SIMPL Frontend Admin](http://localhost:8100/simpl/) but only if you need it!

## Model Schema

![](docs/models.png)
