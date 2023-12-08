""":mod:`ring.django` --- Django support
========================================
"""
from __future__ import absolute_import


from django.core import cache as django_cache
from .func import base as fbase
from .func.sync import CacheUserInterface


__all__ = ("cache",)


def promote_backend(backend):
    """Get string name to Django cache backend."""
    if isinstance(backend, (str, bytes)):
        backend = django_cache.caches[backend]
    return backend


class LowLevelCacheStorage(fbase.CommonMixinStorage, fbase.StorageMixin):
    """Storage implementation for :data:`django.core.cache.caches`."""

    def get_value(self, key):
        value = self.backend.get(key)
        if value is None:
            raise fbase.NotFound
        return value

    def set_value(self, key, value, expire):
        self.backend.set(key, value, timeout=expire)

    def delete_value(self, key):
        self.backend.delete(key)


def cache(
    backend=django_cache.cache,
    key_prefix=None,
    expire=None,
    coder=None,
    user_interface=CacheUserInterface,
    storage_class=LowLevelCacheStorage,
):
    """A typical ring-style cache based on Django's low-level cache API.

    :param Union[str,object] backend: Django's cache config key for
           :data:`django.core.cache.caches` or Django cache object.

    :see: `Django's cache framework: Setting up the cache`_ to configure django
        cache.
    :see: `Django's cache framework: The low-level cache API`_ for the backend.

    .. _`Django's cache framework: Setting up the cache`: https://docs.djangoproject.com/en/2.0/topics/cache/#setting-up-the-cache
    .. _`Django's cache framework: The low-level cache API`: https://docs.djangoproject.com/en/2.0/topics/cache/#the-low-level-cache-api
    """  # noqa
    backend = promote_backend(backend)
    return fbase.factory(
        backend,
        key_prefix=key_prefix,
        on_manufactured=None,
        user_interface=user_interface,
        storage_class=storage_class,
        miss_value=None,
        expire_default=expire,
        coder=coder,
    )
