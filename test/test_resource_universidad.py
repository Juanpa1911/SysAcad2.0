import unittest
from flask import current_app
from app import create_app
from app import db
import os

class resourceUniversidadTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_obtener_todos(self):
        """
        client = self.app.test_client(use_cookies=True)
        #TODO: arreglar esto no se como va bien
        #universidad1 = nuevauniversidad()
        #universidad2 = nuevauniversidad()
        #(acá hay que ingeniarselas para importar el método nuevauniversidad del test_universidad.py)
        response = client.get('http://localgost:5000/api/v1/universidad/')
        self.assertEqual(response.status_code, 200)
        #self.assertIsNotNone(response.get_json())
        """
        pass

if __name__=='__main__':
    unittest.main()