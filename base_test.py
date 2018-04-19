import os
import unittest
import tempfile

import flask_app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        flask_app.app.testing = True
        self.app = flask_app.app.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert b'Hello' in rv.data


if __name__ == '__main__':
    unittest.main()