## Udemy - Create a CRUD Django App 

*Hosted via Heroku at* -  https://myems-project.herokuapp.com/

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
* Another approach is to physically delete the table via pgAdmin. Clean it up by removing related rows in the `django_migrations` and `auth_permission` tables. Delete the unused files in the project `migrations` folder.

#### Database First Approach
* Add `models.py` and `__init__.py` files from `myems` directory to `feedback` directory and delete the migrations folder in `myems`.
* Add `feedback` directory to installed apps in `myems` `settings.py`.
* Make migrations with `python manage.py makemigrations feedback`. and `migrate` as well.
* Use `python manage.py inspectdb` to inspect the DB in an all class format.
* Run `python manage.py inspectdb > myems/models.py` to save. 
* Clean up our new `myems` `models.py`.
* Run `python manage.py makemigrations`.
* Run `python manage.py makemigrations myems`.
* Fake migrations by `python manage.py migrate --fake myems 0001_initial`.


#### Django - QuerySets 
* To open the python shell , type `python` into the terminal.
* To open the django shell, run `python manage.py shell`.
* In the django shell - 

```python
>>> from myems.models import Employee
>>>
>>> querySet = Employee.objects.all()
>>> print querySet
```

* To overide the results of our data from string representations to the actual data, modify the class from `models.py`. Restart and run the code above again in the shell.
* Look at other examples of queries in the `django-queries.md` file.

#### Django - Admin
* Register Django admin for our EMS data.
* Edit custom fields on our admin page to reflect feedback model.
* Create msg box for editing record using custom fields.

##### *Django - Validators*
* docs - https://docs.djangoproject.com/en/1.11/ref/validators/
* Use Django's built in validation for email , max_length etc for our form element. 
* Skip Django Create Custom validators tutorial.
* Add admin custom list filters for employee data.

##### *Django - User View Permissions*
* Add permissions to addional users to be able to edit data.
* Add users - test, test_2, password-Number@123456
* To Add [Django-view-permissions extension](https://github.com/ctxis/django-admin-view-permission).
* Add `admin_view_permission` to our `settings.py` to install.
* Run `pip install django-admin-view-permission`.
* Update `requirements.txt` with `pip freeze > requirements.txt`.
* Run `python manage.py migrate`. If migrations issues exist run `python manage.py migrate --fake-initial`.
* Add our User to a Group to only be able to read Data.

##### *Django - Responsive*
* Install the following package to make our Admin view responsive [Django-Flat-Responsive](https://github.com/elky/django-flat-responsive).
* Run `pip install django-flat-responsive`.
* Add `'flat_responsive',` to our installed apps in `settings.py`.
* To further on the styling add our styling to `venv/Lib/site-packages/flat-responsive/templates/admin/base.html`.

##### *Django - Custom Admin Header*
* Add our custom admin site to our project to change text.


#### Django - URL Configurations & Response Views
*Function based View* -
* Add URL `http://127.0.0.1:8000/employees/1101/profile/`.
* Creare index URL and render with template

*Class based View & Generic* - 
*  Difference in design pattern (http method)
* Add templates and add URLS for CRUD operations on employee data.

 
#### Django - Templates
* Render the material design template with django and edit settings and import the right packages. 


#### Django - Add Images to our DB
* [Django STD -image] (https://github.com/codingjoe/django-stdimage)
* Install with `pip install django-stdimage`.
* Add `'stdimage'` to `installed_apps` in `settings.py`.
* Update with `pip freeze > requirements.txt`.
* Run `makemigrations` and then `migrate` because we have updated models.


### Deploying to Heroku
#### Setting up
* Install Heroku CLI via Installer or npm with `npm install -g heroku-cli`.
* Verify installation with `heroku --version`.
* Add static folder and use run `python manage.py collectstatic`.
* Add [Whitenoise Django](https://github.com/evansd/whitenoise) to serve static files when debug mode is off for production. Run `pip install whitenoise`.
* Whitenoise Django docs - [http://whitenoise.evans.io/en/stable/django.html].
* Install Gunicorn Production server with `pip install gunicorn`.
* Install `pip install dj-database-url`.
* Update with `pip freeze > requirements.txt`.
* Add `runtime.txt` and `Procfile`.

#### Deployment
* Log in to Heroku via `heroku login`.
* Make sure you have a `git` repo initialized.
* Create heroku app with `heroku create myems`.
* Open app with `heroku open`.
* To configure our Db - `heroku config`
* To link up our Db to Heroku use `heroku pg:backups restore "https://www.dropbox.com/s/wsdftd8021xx9ew/employee_db_small_heroku_final.backup?dl=1" --confirm myems-project`
* To verify use `heroku pg:psql` and type `select (*) from employees;`.
* Check hosted link.

### Deploying to Amazon S3
#### Setting up
* 