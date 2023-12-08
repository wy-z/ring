import django
from django.core.cache import caches
import ring

from . import django_app  # noqa: F401

django.setup()


def test_django_cache():
    @ring.django.cache("default", expire=1)
    def f(a):
        return a * 100

    assert f.get(10) is None
    assert f(10) == 1000
    raw_key = f.key(10)
    assert caches["default"].get(raw_key) == f.get(10)

    @ring.django.cache()
    def f(a):
        return a * 50

    assert f.get(10) == 1000
    caches["default"].delete(raw_key)
    assert f(10) == 500
    f.delete(10)
    assert caches["default"].get(raw_key) is None
