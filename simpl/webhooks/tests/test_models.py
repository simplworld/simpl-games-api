from test_plus.test import TestCase

from ..factories import (
    SubscriberFactory, ErroringSubscriberFactory, ConnectedSubscriberFactory
)


class SubscriberModelTests(TestCase):

    def test_simple_creation(self):
        SubscriberFactory()
        ErroringSubscriberFactory()
        ConnectedSubscriberFactory()

    def test_record_error(self):
        s = SubscriberFactory()
        s.record_error(status=500, content="Server Error")
        self.assertTrue(s.erroring)
        self.assertIsNotNone(s.last_error)
        self.assertEqual(s.last_error_status, 500)
        self.assertEqual(s.last_error_content, "Server Error")

    def test_record_with_invalid_status_code(self):
        s = SubscriberFactory()
        s.record_error(status="wheee", content="Super Error")
        self.assertIsNone(s.last_error_status)
        self.assertTrue("INVALID" in s.last_error_content)

    def test_clear_error(self):
        e = ErroringSubscriberFactory()
        e.clear_error()
        self.assertFalse(e.erroring)

    def test_record_connect(self):
        s = SubscriberFactory()
        self.assertFalse(s.connected)
        s.record_connect()
        self.assertTrue(s.connected)