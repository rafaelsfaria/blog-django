[![Build Status](https://travis-ci.com/rafaelsfaria/blog-django.svg?branch=master)](https://travis-ci.com/rafaelsfaria/blog-django)

# Blog app with Django (python), html/css/js, postgreSQL

Features: Register, login, create new posts

Models: User, Post, Category

Requirements: python3 and pip3

Clone this repo and create a new virtual environment

On windows:
```sh
virtualenv env
.\env\Scripts\activate
pip install requirements.txt
py manage.py runserver
```

On linux:
```sh
virtualenv env
source /env/bin/activate
pip3 install requirements.txt
python3 manage.py runserver
```