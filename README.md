[![Python Support](https://img.shields.io/badge/python-3.6-blue.svg)]()
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/09e269d7f2414f2581cbcf34da1abdf9)](https://www.codacy.com/app/seLain/Django-Eel?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=seLain/Django-Eel&amp;utm_campaign=Badge_Grade)
[![Code Health](https://landscape.io/github/seLain/Django-Eel/master/landscape.svg?style=flat)](https://landscape.io/github/seLain/Django-Eel/master)
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

# Django-Eel

Django-Eel is a Django App for HTML GUI applications, with easy Python/JS interoperation. It is a porting version of [Eel](https://github.com/ChrisKnott/Eel).

### Repo branches

 - **master** : the master branch of Django-Eel
 - **eel-master** : keeping sync with [Eel](https://github.com/ChrisKnott/Eel)/master

### Requirements

 - Django ( >=2.0.7 recommended )
 - channels ( >=2.1.2 recommended )
 - gevent ( >=1.3.4 recommended )

### Getting Started

#### Installation

Download Django-Eel package from GitHub and install:
```
python setup.py install
```
Or install through PIP:
```
pip install django-eel
```
Alternatively by git source for latest version:
```
pip install git+https://github.com/seLain/django-eel
```

#### Create demo project

Create an empty django project:
```
django-admin startproject demo
```
Create examples django app:
```
django-admin startapp example
```
Add **channels**, **django_eel**, and **example** to **demo/settings.py**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'django_eel',
    'example',
]
```
Set ASGI_Application in **demo/settings.py**. It is required by channels.
```python
WSGI_APPLICATION = 'demo.wsgi.application'
ASGI_APPLICATION = "demo.routing.application"
```
Add **routine.py** under **demo** project root. The **routine.py** routes websocket requests to **EelConsumer**.
```python
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django_eel.consumers import EelConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "websocket": URLRouter([
        url(r"^eel$", EelConsumer), # do not alter this line
    ]),
})
```
Configure demo\urls.py to route http request to eel and example respectively.
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^eel/', include('django_eel.urls')), # do not alter this line
    url(r'^example/', include('example.urls')), # set by your app name
]
```
That's the configuration part. Now we add a helloword example.

#### Create template and view

Create **example\templates\example\hello.html** :
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hello, World!</title>
        
        <!-- request for eel.js from django-eel, do not alter this line -->
        <script type="text/javascript" src="/eel/eel.js"></script>
        <script type="text/javascript">
        
        eel.expose(say_hello_js);               // Expose this function to Python
        function say_hello_js(x) {
            console.log("Hello from " + x);
        }
        
        say_hello_js("Javascript World!");
        eel.say_hello_py("Javascript World!");  // Call a Python function
        
        </script>
    </head>
    
    <body>
        Hello, World!
    </body>
</html>
```
This **hello.html** is almost the same as the original [Eel](https://github.com/ChrisKnott/Eel) example, except the request for **eel.js**.

Then we create the view 
```python
from django.shortcuts import render
import django_eel as eel

# initialize eel
eel.init('example/templates/example')

###########################
# Hello example
###########################
def hello_page(request): # accept request for hello.html
	return render(request, 'example/hello.html')

@eel.expose
def say_hello_py(x):
	print('Hello from %s' % x)
	eel.say_hello_js('Python3 and Django World!') # call js function

###########################
# Open local browser
###########################
eel.start('example/hello', size=(300, 200)) # optional for off-line browsing
```

Finally, we have to set **example\urls.py** to handle the request to example pages.
```python
from django.conf.urls import url

from .views import hello_page

urlpatterns = [
    url(r'^hello$', hello_page),
]
```

#### Running the demo

Simply run the django project as usual:
```
python manage.py runserver
```
A browser windows should popup if this line is added in view.
```python
eel.start('example/hello', size=(300, 200))
```
You can also access the hello example by browser:
```
http://localhost:8000/example/hello
```
That's it. All behaviors are basically the same as the original [Eel](https://github.com/ChrisKnott/Eel).
