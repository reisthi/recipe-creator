# Recipe Creator App

Django REST framework application to create/update/delete users and their recipes through API calls.

Recipes are composed of the following:
- Ingredients
- Steps 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt

```

## Usage
```bash
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver
```
