# django-crm
CRM (Customer Relationship Management) App with Django, Python, and MySQL.

# Virtual Env

```
python3 -m venv virt
source virt/bin/activate
```

# Installing django and mysql-connectors
```
pip3 install django
pip3 install mysql-connector-python
```

# Starting Project and app
```
$ django-admin startproject dcrm
$ cd dcrm
$ python3 manage.py startapp website
```

# Adding application to setting.py
```
Add the previosuly created app (website), in the INSTALLED_APPS section of setting.py file inside the dcrm/dcrm/settings.py file. 
Also configure the database section. 
Create a mydb.py file in the project directory.
```

# Migration
```
$ python3 manage.py migrate
```
# Creating a superuser
```
$ python3 manage.py createsuperuser
```
# Starting django application
```
$ python3 manage.py runserver
```