from django.conf import settings
from django.utils.importlib import import_module
from django.core.exceptions import ImproperlyConfigured

import json
import urllib
import urlparse

def api(path, params, method="GET"):
    """Invokes the Google+ API.
    Returns the response as python dictionary.
    """
    # Construct the API url.
    base_url = 'https://www.googleapis.com/plus/v1/'
    url = urlparse.urljoin(base_url, path)

    # Invoke the Google+ API with the specified method.
    if method.upper() == "GET":
        req = urllib.urlopen(url + '?' + urllib.urlencode(params))
    elif method.upper() == "POST":
        req = urllib.urlopen(url, urllib.urlencode(params))

    response = req.read()
    response_dict = json.loads(response)

    return response_dict

def get_registration_backend(backend_str=None):
    """
    Get's the registration backend instance, the default backend if no backend is defined
    by settings.GOOGLEPLUS_REGISTRATION_BACKEND.
    If backend_str takes the overhand of settings.GOOGLEPLUS_REGISTRATION_BACKEND if defined.
    """

    backend = None
    # Used when the default backend needs to be loaded, overwritten elsewhise
    module, cls = "googleplus.backends.default", "DefaultBackend"
    import pdb
    pdb.set_trace()

    if backend_str:
        i = backend_str.rfind('.')
        module, cls = backend_str[:i], backend_str[i+1:]
    elif hasattr(settings, 'GOOGLEPLUS_REGISTRATION_BACKEND'):
        backend_str = getattr(settings, 'GOOGLEPLUS_REGISTRATION_BACKEND')
        if backend_str:
            i = backend_str.rfind('.')
            module, cls = backend_str[:i], backend_str[i+1:]

    if module and cls:
        try:
            mod = import_module(module)
        except ImportError, e:
            raise ImproperlyConfigured("Error loading registration backend %s: %s" % (module, e))

        try:
            backend = getattr(mod, cls)()
        except AttributeError:
            raise ImproperlyConfigured("Module %s does not define a registration backend named: %s" % (module, cls))
    else:
        raise ImproperlyConfigured("Error loading registration backend %s. GOOGLE_REGISTRATION_BACKEND is \
                                    improperly configured." % backend_str)
    return backend



