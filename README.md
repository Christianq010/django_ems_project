## Udemy - Create a CRUD Django App 

### Getting Set up

### Installations
* python 2.7 - 
* postgreSQL -  
* pgAdmin - 
* virtualenv- 


#### Virtual Environment - virtualenv 
* Create our virtual environment to install python packages just for this project in a folder we can name as `venv` with `virtualenv venv`.
* On windows to run our virtual environment within GitBash -  `source venv/Scripts/activate`

##### Using Django with virtualenv
* Install django within the virtual env with `pip install django`
* To create a project within our venv environment and folder - `django-admin startproject myems .`
* To print out the current packages you've installed within your virtual enviroment `pip freeze`.
* Create a `requirements.txt` file with all dependencies with `pip freeze > requirements.txt`.

* Note: to install a project based on the `requirements.txt` file 
```
pip install -r requirements.txt
```
