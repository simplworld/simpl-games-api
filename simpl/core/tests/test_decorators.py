from django.core.cache import cache
from test_plus.test import TestCase

from simpl.core.decorators import cached_method


class TestDecorators(TestCase):
    def test_cached_method(self):
        class A(object):
            slug = 'test-object'

            @property
            @cached_method("unique:key:{.slug}")
            def foo(self):
                return 'x'

        t = A()
        self.assertEqual(t.foo, 'x')

        cached = cache.get("unique:key:test-object")
        self.assertEqual(cached, 'x')
