# django-tdd-apis

<div align='center'>

[![Django CI](https://github.com/lorbic/django-tdd-apis/actions/workflows/django.yml/badge.svg)](https://github.com/lorbic/django-tdd-apis/actions/workflows/django.yml)

</div>

Creating APIs with django using Test Driven Development (TDD)

Read `env.template` for _dotenv_ configuration

## Run Tests

```py
$ python manage.py test && flake8
```

> If you get following error:  
> **Got an error creating the test database: permission denied to create database**  
> Then change permission to your **postgres database user** by executing following command &nbsp;` alter role djangouser createdb;`&nbsp;.  
> Or you can use default **sqlite** database.
