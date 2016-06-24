# EasyStatus
[![TravisCI](https://travis-ci.org/leonardoarroyo/easystatus.svg)]((https://travis-ci.org/leonardoarroyo/easystatus))

EasyStatus was born as simple open source alternative to StatusPage.io, Status.io and CachetHQ.

## Getting Started

Running EasyStatus locally is very straightforward. It's built on top of Django.  
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

The project was developed and test on Python 3.5. Other versions weren't tested.
- python 3.5
- virtualenv and virtualenvwrapper

### Installing

Let's start by creating a virtualenv

```
mkvirtualenv easystatus
workon easystatus
```

Now clone the project

```
git clone https://github.com/leonardoarroyo/easystatus
```

Installing dependencies

```
cd easystatus
pip install -r requirements.xt
```

Copy environment variable and edit them

```
cat environment.sample.sh >> ~/.virtual_envs/easystatus/bin/postactivate
vim ~/.virtual_envs/easystatus/bin/postactivate
```

Reload your virtualenv

```
workon easystatus
```

Migrate

```
python manage.py migrate
```

Finally, start the server!

```
python manage.py runserver
```


The server should now be running on ```http://localhost:8000```.  
The API endpoints are on ```/api/```.  
The API endpoints documentation are on ```/docs/```.  

## Running the tests

Test the entire project

```
python manage.py test
```

## Deployment

This project can be deployed like any Django app. Please check [Django docs](https://docs.djangoproject.com/en/1.9/howto/deployment/) for more information.

## Built With

* Django
* django-rest-framework

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Leonardo Arroyo** - *Initial work* - [leonardoarroyo](https://github.com/leonardoarroyo)

See also the list of [contributors](https://github.com/leonardoarroyo/easystatus/contributors) who participated in this project.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details

