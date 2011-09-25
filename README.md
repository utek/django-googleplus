Django-googleplus is a fork of django-custom-auths without facebook support.
This django application solely provides googleplus user registration.
The applications design is largely modeled after django-registration which,
provides a pluggable backend system.


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


    `AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'googleplus.backends.GooglePlusBackend',
    )`

* Add your google account credentials to your settings.py file.
You can get these settings from google [here](https://code.google.com/apis/console/).
    `GOOGLE_CLIENT_ID=<cllient-id>
    GOOGLE_CLIENT_SECRET=<client-secret>`


