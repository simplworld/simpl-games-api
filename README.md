# Simpl Games Framework API Project

This project uses Python 3.6.x and Django 1.9.x

## Getting Started

### To setup Vagrant box with PostgreSQL

```bash
$ git clone git@github.com:simplworld/python-vagrant-centos7.git
$ cd python-vagrant-centos7
$ vagrant up
```

### Setup simpl-games-api

```bash
$ cd python-vagrant-centos7/projects
$ git clone git@github.com:simplworld/simpl-games-api.git

$ vagrant ssh
$ mkvirtualenv simpl-games-api
$ add2virtualenv /vagrant/projects/simpl-games-api
```

### Python Setup (assumes working in vagrant)

```bash
$ cd projects/simpl-games-api
$ pip install -r requirements.txt
```

### Create PostgreSQL database

Create a database:

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
$ ./manage.py create_simpl_user
```

This creates a super user with id 'simpl@simpl.world' and password 'simpl' and ensures test users can be assigned passwords in scripts.

### Settings setup

Setup the `DJANGO_SETTINGS_MODULE` to use:

```bash
$ export DJANGO_SETTINGS_MODULE=config.settings.local
```

### Start the web server

Django's `runserver` does not support `Keep-Alive` requests, so we use `gunicorn` instead. A command to run gunicorn is included in `simpl-games-api`:

```bash
$ ./manage.py run_gunicorn 0.0.0.0:8100
```

### Run tests

Run `py.test`:

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

If you are using an environment that supports running Pillow, uncomment the Pillow line in requirements.txt and run:

```
$ pip install -r requirements.txt --upgrade
$ ./manage.py graph_models games -o docs/models.png
```

## What's where?

- [API Docs](http://localhost:8100/)
- [Simpl apis](http://localhost:8100/apis/)
- [Django Admin](http://localhost:8100/admin/)
- ~~[Simpl Frontend Admin](http://localhost:8100/simpl/) but only if you need it!~~

## Model Schema

![](docs/models.png)

## Check Deployed System

We have a simple management command which will check DNS, HTTP/HTTPS connectivity in general, ability to login to the admin, that the API responds properly and that the game slug in question is installed.  To use this command you **MUST** have a valid admin login to use the command.

Simple usage:

```
manage.py check_deploy https://simpl.mine.ed/
```

The command will prompt you for your admin user's email address (aka username), password, and game slug.  Or you can provide them on the command line like this: 

```
manage.py check_deploy https://simpl.mine.ed/ --email='me@mine.ed' --password='sumpun' --game=sim
```

# Deploying on LL Kubernetes development cluster


# Kubernetes Deployment

## TL;DR section

### setup the `kubectl` environment

#### show current cluster contexts

```
#: kubectl config get-contexts
```

#### select different cluster (if needed)

```
#: kubectl config use-context <cluster-name>
```

#### select different default namespace  (if needed)

```
#: kubectl config set-context <cluster-name> --namespace=simpl
```

### upgrade dev deployment
```
:#  helm upgrade --set=ImageTag=<target docker image tag> simpl-api-dev kube/simpl-games-api
```

### upgrade production deployment

```
:#  helm upgrade --set=ImageTag=<target docker image tag> -f kube/simpl-games-api/prod_values.yaml simpl-api-prod kube/simpl-games-api
```

## run kubectl web console

```
:#  kubectl proxy
```

Browse to http:/localhost:8001/ui
