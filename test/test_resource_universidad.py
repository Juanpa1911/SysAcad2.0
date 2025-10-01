import unittest
from flask import current_app
from app import create_app
from app import db
from test.instancias import nuevaUniversidad
import os

class resourceUniversidadTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_obtener_todos(self):
        
        client = self.app.test_client(use_cookies=True)
        #TODO: arreglar esto no se como va bien
        universidad2 = nuevaUniversidad()
        universidad1 = nuevaUniversidad()
        #(acá hay que ingeniarselas para importar el método nuevauniversidad del test_universidad.py)
        response = client.get('http://localhost:5433/api/v1/universidad')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        
        # pass

if __name__=='__main__':
    unittest.main()