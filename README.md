# coding_test
Coding Test submission.

## Initia Setup

1. Download [Python](https://www.python.org/downloads/) and Install it.

``` bash

# python version 3.9.7

```

2. Install [PIP and Virtual Environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) on your machine.

``` bash
# check/upgrade latest pip

python3 -m pip install --user --upgrade pip

python3 -m pip --version

# install virtualenv

python3 -m pip install --user virtualenv


```


2. Clone the Repository on your IDE

``` bash
# clone link
git clone https://github.com/omar115/coding_test.git

```

3. Activate Virtual Environment and Install Dependencies

``` bash

# create venv
python3 -m venv env

# activate venv

source env/bin/activate

# install packages 

pip install -r requirements.txt


```

4. Connect Database and Start the Django Server

``` bash

# open your IDE terminal and run the following commands

# database used -> SQLite3

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```

5. API Endpoints to Test

``` bash

# create parent user
http://127.0.0.1:8000/api/parent/create/

# delete parent user
http://127.0.0.1:8000/api/parent/delete/<id>/

# update parent user
http://127.0.0.1:8000/api/parent/update/<id>/


# create child user
http://127.0.0.1:8000/api/child/create/

# delete child user
http://127.0.0.1:8000/api/child/delete/<id>/

# update child user
http://127.0.0.1:8000/api/parent/update/<id>/

```
