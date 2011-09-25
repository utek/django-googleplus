import os
import sys

BASE_DIRECTORY = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIRECTORY)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Subhranath Chunder', 'subhranath@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_custom_auths.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Kolkata'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

ROOT_URLCONF = 'urls'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fb67krjjfdhlpkdq#r&qhv#7^e&+&1=3((01li&xu+g)!g)t!@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIRECTORY, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    #'registration',
    'shell+',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'account',
    #'facebook',
    'googleplus',
)

REGISTRATION_BACKEND='registration.backends.default.DefaultBackend'
GOOGLEPLUS_REGISTRATION_BACKEND='googleplus.backends.default.DefaultBackend'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
#L#O#G#G#I#N#G #= #{
    #'#v#e#r#s#i#o#n#'#: #1#,
    #'#d#i#s#a#b#l#e#_#e#x#i#s#t#i#n#g#_#l#o#g#g#e#r#s#'#: #F#a#l#s#e#,
    #'#f#i#l#t#e#r#s#'#: #{
        #'#r#e#q#u#i#r#e#_#d#e#b#u#g#_#f#a#l#s#e#'#: #{
            #'#(#)#'#: #'#d#j#a#n#g#o#.#u#t#i#l#s#.#l#o#g#.#C#a#l#l#b#a#c#k#F#i#l#t#e#r#'#,
            #'#c#a#l#l#b#a#c#k#'#: #l#a#m#b#d#a #r#: #n#o#t #D#E#B#U#G
        #}
    #}#,
    #'#h#a#n#d#l#e#r#s#'#: #{
        #'#m#a#i#l#_#a#d#m#i#n#s#'#: #{
            #'#l#e#v#e#l#'#: #'#E#R#R#O#R#'#,
            #'#f#i#l#t#e#r#s#'#: #[#'#r#e#q#u#i#r#e#_#d#e#b#u#g#_#f#a#l#s#e#'#]#,
            #'#c#l#a#s#s#'#: #'#d#j#a#n#g#o#.#u#t#i#l#s#.#l#o#g#.#A#d#m#i#n#E#m#a#i#l#H#a#n#d#l#e#r#'
        #}
    #}#,
    #'#l#o#g#g#e#r#s#'#: #{
        #'#d#j#a#n#g#o#.#r#e#q#u#e#s#t#'#: #{
            #'#h#a#n#d#l#e#r#s#'#: #[#'#m#a#i#l#_#a#d#m#i#n#s#'#]#,
            #'#l#e#v#e#l#'#: #'#E#R#R#O#R#'#,
            #'#p#r#o#p#a#g#a#t#e#'#: #T#r#u#e#,
        #}#,
    #}
#}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'googleplus.backends.GooglePlusBackend',
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

GOOGLEPLUS_CLIENT_ID = '416079500309@developer.gserviceaccount.com'
GOOGLEPLUS_CLIENT_SECRET = 'iCkjIUfmdfZRF2jZfn2EqIgV'
