# djportfolio
Yet another Django Project!!!


### Create a folder
`mkdir <projectname>`
### Make a Virtualenv 
_(optional '.' before folder name will make it hidden)_</br>
`python3 -m venv .<venv name>`
### Activate Virtualenv
`source .<venv name>/bin/activate`
### Install Django
`pip install django`
### Pip freeze confirms the modules installed in your new virtualenv
`pip freeze`
### Create Django project 
_('.' at the end puts folder directly in main directory, avoiding further nesting)_</br>
`django-admin startproject <projectname> .`
### Start the server
`python manage.py runserver`
### Create first app
`python manage.py startapp <appname>`

##### Open in your fav IDE (VSCode or PyCharm)
