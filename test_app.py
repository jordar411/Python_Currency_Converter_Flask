from unittest import TestCase
from app import app
from flask import session


class AppTestCase(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_show_form(self):
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<button>Convert</button>', response.data)
