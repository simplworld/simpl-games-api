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

```bash
$ ./manage.py graph_models games -o docs/models.png
```

## What's where?

- [API Docs](http://localhost:8100/)
- [Simpl apis](http://localhost:8100/apis/)
- [Django Admin](http://localhost:8100/admin/)
- ~~[Simpl Frontend Admin](http://localhost:8100/simpl/) but only if you need it!~~

## Model Schema

![](docs/models.png)

# Deploying on LL Kubernetes development cluster

To configure yourself to be pointing at the correct cluster run:
```
kubectl config use-context <cluster>
kubectl config set-context <cluster> --namespace=<namespace where you’ll be working>
```

where cluster is a Kubernetes cluster name in your ~/.kube/config

Once CI has built the new image and it is pushed to the Docker registry, run:
```

helm upgrade simpl-api-dev kube/simpl-games-api

```
For the production cluster use:

```

helm upgrade -f kube/simpl-games-api/prod_values.yaml --set=ImageTag=<image-tab> simpl-api-prod kube/simpl-games-api/

```

For example, if you were deploying `v1.0.0` you would run ```helm upgrade -f kube/simpl-games-api/prod_values.yaml --set=ImageTag=v1.0.0 simpl-api-prod kube/simpl-games-api/```

## Check Deployed System

We have a simple management command which will check DNS, HTTP/HTTPS connectivity in general, ability to login to the admin, that the API responds properly and that the game slug in question is installed.  To use this command you **MUST** have a valid admin login to use the command.

Simple usage:

```
manage.py check_deploy https://simpl.dev.wharton.revsys.com/
```

The command will prompt you for your admin user's email address (aka username), password, and game slug.  Or you can provide them on the command line like this: 

```
manage.py check_deploy https://simpl.dev.wharton.revsys.com/ --email='frank@revsys.com' --password='secret!' --game=roe
```