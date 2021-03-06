# Baires Dev

## Requirements

The main requirements are:

- Python 3.6+
- Django 2.1
- Django Rest Framework 3.8

You can see the other requirements inside the requirements files.

## Installing

To install this project you can use `pip` or download individually which library from PyPI.

Using `pip`, you can run the following commands for each environment you want:

```bash
pip install -r requirements/local.txt
pip install -r requirements/production.txt
pip install -r requirements/test.txt
```

## Setting Up

The `development` environment is using SQLite by default, to make easier to run and test the project. 
However, you can chagen the Database in `settings/local.py`. The `production` environment is set to use 
PostgreSQL, it is just needed to fill the dictionary with all the information.

After setup the DB, you need to run the following commands to have the data scheme right.

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Running

To run this project, you can just run the following command:

```bash
python manage.py runserver
```

This command will run the project in `development` mode.

You can access the admin page by `http://localhost:8000/admin` and using the previous created superuser. 
Then, you can manage the users and their access tokens.