from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
       url(r'login/$', 'django_googleplus.views.login_handler', { 'backend': 'googleplus.backends.default.DefaultBackend'}),
)
