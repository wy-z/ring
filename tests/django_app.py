"""Django sample app to test ring features.

To run as a stand-alone app, run:

.. code-block:: sh

    django-admin runserver --pythonpath=. --settings=django_app

"""
import random
import string
from django.conf import settings


SECRET_KEY = "".join(
    random.choice(string.ascii_lowercase + string.digits) for _ in range(40)
)

SETTINGS = dict(
    DEBUG=False,
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["127.0.0.1", "localhost", "testserver"],
)

globals().update(SETTINGS)  # django-admin support
settings.configure(**SETTINGS)  # module import support
