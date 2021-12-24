# Django Blog Tutorial Project
In that project I try to learn to build a website with python-django and bootstrap. I will add a documentation soon. Besides, you can start to create your own website. 
However, please do not think that documentation is enough for you. Please continue to search and to learn.

## Requirements
1. Django - 3.2.10  
2. PIL - 8.4.0 - 
3. Bootstrap - 5.1.3 
4. Ckeditor - 6.2.0 - `pip install ckeditor==6.2.0`
5. Crispy Forms - 1.13.0 - `pip install django-crispy-forms`

## Installation
You can use any Python Editor or IDE. However I suggest you use Visual Studio Code due to support many language at the same time and git repository feature.
We need a virtual environment due to isolate all other python libraries. Hence, we can get a clear developing area for our project.<br/>
So, install the virtualenv library if you dont have. `pip install virtualenv`.<br/>
Go to the directory which you want to develop the project.
Create virtual environment - `virtualenv env_name`.<br/>
Activate the environment - `env_name\Scripts\activate`.<br/>
Install django 3.2.10 - `pip install django==3.2.10`.<br/>
Install PIL 8.4.0 - `pip install pillow==8.4.0`.<br/>

## Progress
You can use my project or you can build your project.<br/>
Let's create a django project.
`django-admin startproject project_name`. or `django-admin startproject project_name .`. With dot the project build at the same directory.

If you wish, you can change timezone and languge in settings.py file.

Let's start the local server, `python manage.py runserver`.

At the begin, django gives us some applications like admin interface. However, we can not use them right now.
First we have to add them database - `python manage.py migrate`.

We can use apps which exist. Let's go to admin panel to see what we have. However, we don't have any user.<br/>
Add a superuser - `python manage.py createsuperuser`.
After that command enter a username and password.

Here is the our admin page. http:127.0.0.1:8000/admin

In programming we can write all codes in one script but this not a good way to develop a project. Therefore, we will split the project to the scripts. 
When we do that, we will notice there are same scripts with similar duty and names. So, to get rid of that complexity we will create applications.

For blog website, post structure is an app.
Let't create an app. `python manage.py startapp app_name`.

<br/>
Continue . . .

