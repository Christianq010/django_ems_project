## Udemy - Create a CRUD Django App 

### Getting Set up

### Installations
* python 2.7 - 
* postgreSQL -  
* pgAdmin - 
* virtualenv- 

#### Additional Resources 
* psycorpg - http://initd.org/psycopg/

#### Setting up our Database
* 

#### Virtual Environment - virtualenv 
* Create our virtual environment to install python packages just for this project in a folder we can name as `venv` with `virtualenv venv`.
* To run our virtual environment within GitBash /Linux -  `source venv/Scripts/activate`
* On windows to run our virtual environment -  `venv\Scripts\activate.bat`
* To deactivate - `source venv\Scripts\deactivate`

##### Using Django with virtualenv
* Install django within the virtual env with `pip install django`
* To create a project within our venv environment and folder - `django-admin startproject myems .`
* To print out the current packages you've installed within your virtual enviroment `pip freeze`.
* Create a `requirements.txt` file with all dependencies with `pip freeze > requirements.txt`.

* Note: to install a project based on the `requirements.txt` file 
```
pip install -r requirements.txt
```

* Edit main `settings.py` to include the following code for paramters we specified when setting up our database.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {'options': '-c search_path=public'},
        'NAME': 'employees',
        'USER': 'postgres',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

* Run `pip install django psycopg2` to install psycopg2 within the virtual environment.
* Update `requirements.txt` file with all dependencies with `pip freeze > requirements.txt`.
* Run server with `python manage.py runserver` to check if our app is connected succesfully.
* Note: Change default on server with `python manage.py runserver 8083`.
* Make migrations `python manage.py migrate`.
* Control the state of our Db migrations with `python manage.py makemigrations myems`.

* To use our admin panel, create a super user with `python manage.py createsuperuser` (User: admin, email: christianq010@gmail.com, password: ******)


#### Django - Models 
##### Model First Approach

* Add the `models.py` file to our `ems` folder and add our imports and classes.
* Use [Django meta Data docs](https://docs.djangoproject.com/en/1.11/ref/models/options/) to name table or order by etc.
* In the virtual environment run `python manage.py makemigrations myems`.
* To find out what SQL command was be executed by Django run `python manage.py sqlmigrate myems 0001_initial`.
* Run migrate after making migrations with `python manage.py migrate`.
* To add or remove a column after initially setting up the table, just run `makemigrations` & `migrate` command again and new migrations files will be created.

*Deleting tables*
* One approach is commenting out the class and running `makemigrations` and `migrate` commands again.
* Another approach is to hpysically delete the table via pgAdmin. Clean it up by removing related rows in the `django_migrations` and `auth_permission` tables. Delete the unused files in the project `migrations` folder.

##### Database First Approach