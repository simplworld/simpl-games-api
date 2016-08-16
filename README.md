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
clone simpl-games-api inside python-dev-centos7/html directory

$ mkvirtualenv simpl-games-api
$ add2virtualenv /vagrant/html/simpl-games-api
```

### Python Setup (assumes working in python-dev-centos7 vagrant)

```bash
$ cd /vagrant/html/simpl-games-api
$ pip install -r requirements.txt
```

### Settings setup

Setup your `DJANGO_SETTINGS_MODULE` to use:

```bash
$ export DJANGO_SETTINGS_MODULE=config.settings.local
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

### Start the web server

```bash
$ ./manage.py runserver 0.0.0.0:8100
```

### Running tests

```bash
$ py.test
```

Do not commit code if tests are failing.

## What's where?

- [API Docs](http://localhost:8100/docs/)
- The [SIMPL api](http://localhost:8100/apis/)
- [SIMPL Frontend Admin](http://localhost:8100/simpl/)
- [Django Admin](http://localhost:8100/admin/) but only if you need it!

## Model Schema

![](docs/models.png)
