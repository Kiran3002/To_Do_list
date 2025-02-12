1.creating virtual-env   python.exe -m venv venv
2.activating env    venv\scripts\activate
3. install django   pip install django
4. create project   django-admin startproject todolist
5.create app        python manage.py startapp todo
6. create folders    templates,static,media
7. create readme file   readme.md


.................

explaination of files and folders
__init__.py   - To convert project to package
asgi.py,wsgi.py  - To for deployment of project
settings.py  - to configure the data base
urls.py  - To design URLs for an app
models.py  - To specify tables and columns in the database
views.py  - writing business logic in our app
templates - to store the html or frontend files of our project
static - to store the css files of our project
media  - to store the images and videos used in the folder
readme.md - to add documentation of project