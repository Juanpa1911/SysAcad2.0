import unittest
from flask import current_app
from app import create_app
from app.models.facultad import Facultad
from test.base_test import BaseTestCase
import os

class AppTestCase(BaseTestCase):
    
    def test_facultad(self):
        facultad = Facultad()

if __name__ == '__main__':
    unittest.main()
