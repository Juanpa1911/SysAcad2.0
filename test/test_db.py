import os
import unittest
from sqlalchemy import text
from app import create_app, db
from test.base_test import BaseTestCase


class ConnectionTestCase(BaseTestCase):

    # test connection to db
    def test_db_connection(self):
        result = db.session.query(text("'Hello world'")).one()
        self.assertEqual(result[0], 'Hello world')
    
if __name__ == '__main__':
    unittest.main()
