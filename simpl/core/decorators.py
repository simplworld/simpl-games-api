from functools import wraps

from django.core.cache import cache


def cached_method(key, timeout=None):
    """
    Use django's cache to store the result of the method.

    Arguments:
    * `key`: Required. The cache key to use. It will be interpolated with the object instance.
    * `timeout`: Optional.

    Example::

        class MyClass(object):
            name = 'uniquename'

            @cached_method("things:{.name}:color")
            def color(self):
                # The cache key will be "things:uniquename:color"
                return 'brown'
    """
    def decorator(func):
        @wraps(func)
        def wrap(obj, *args, **kwargs):
            _key = key.format(obj)
            value = cache.get(_key)
            if value is None:
                value = func(obj, *args, **kwargs)
                cache.set(_key, value, timeout)
            return value
        return wrap
    return decorator
