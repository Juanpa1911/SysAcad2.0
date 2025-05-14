import unittest
from flask import current_app
from app import create_app
import os
from app.models.departamento import Departamento
class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_departamento_creation(self):
        departamento = Departamento()
        departamento.nombre = "Secretaria"
        self.assertIsNotNone(departamento)
        self.assertEqual(departamento.nombre, "Secretaria")
        self.assertIsNotNone(departamento.nombre)   
    
if __name__ == '__main__':
    unittest.main()