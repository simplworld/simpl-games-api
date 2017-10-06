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


#### select cluster

```

#: kubectl config use-context <cluster-name>

```

#### set default namespace

```

#: kubectl config set-context <cluster-name> --namespace=simpl

```

### upgrade production deployment 

```

:#  helm upgrade simpl-api-prod -f kube/simpl-games-api/prod_values.yaml --set=ImageTag=<target docker image tag> kube/simpl-games-api

```

### upgrade dev deployment
```

:#  helm upgrade simpl-api-dev kube/simpl-games-api

```

----

### Why the difference between dev and prod deployment?

 * Helm reads (by default) <chart-name>/values.yaml
 * Most deployments will be _dev_ environment deployments which is slated to include any test-passing, tagged image
   * for the same reasons, `kube/*/values.yaml` **is** targetted by **bumpversion** for the purpose of adjusting the `ImageTag` key
   * for the same reasons, `kube/*/prod_values.yaml` **is not** targetted by **bumpversion** and thus requires the additional `--set` argument

