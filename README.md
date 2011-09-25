Django-googleplus is a fork of django-custom-auths without facebook support.
This django application solely provides googleplus user registration.
The applications design is largely modeled after django-registration which,
provides a pluggable backend system. A pluggable backend registration system allows
you to create custom backends with custom workflows for registering new users.


# Installation
From github
-----------
    pip install git+https://<username>@github.com/jonasgeiregat/django-googleplus.git
From Pypi
-----------
    A package will be released soon


# setup
* Add 'googleplus' to INSTALLED_APPS in your settings.py file.
* Add AUTHENTICATION_BACKENDS to your settings.py file.


```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'googleplus.backends.GooglePlusBackend',
)
```

* Add your google account credentials to your settings.py file.
You can get these settings from google [here](https://code.google.com/apis/console/).

````python
GOOGLE_CLIENT_ID=<cllient-id> 
GOOGLE_CLIENT_SECRET=<client-secret>
```

* Setup the url to redirect after a successful login session.
Put LOGIN_REDIRECT_URL in settings.py.

```python
LOGIN_REDIRECT_URL='/account/profile'
```


* Setup your url's. 
** Add the following line to your urls.py file.
This will make localhost/googleplus/login the default url to login or register through googleplus services.
    
```python
    url(r'googleplus', include('googleplus.urls'))
```

* Alternatively you can also create your own url setup by pointing your url to the googleplus.views.login_handler method.

```python
    url(r'google/login', 'googleplus.views.login_handler')
```

# What about those registration backends ?
Todo.


# Todo 
README.md file still needs some work.
