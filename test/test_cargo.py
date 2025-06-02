import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo

class CargoTestCase(unittest.TestCase):
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
        
    def test_autoridad_creation(self):
        cargo = self.__nuevoCargo()
        self.__assertCargo(cargo)
        db.session.add(cargo)
        db.session.commit()
        self.__assertCargo(cargo)
        
    
        
        
        
        
    def __nuevoCargo(self):
        cargo = Cargo()
        cargo.categoria_cargo = CategoriaCargo(nombre="Categoria 1")
        cargo.nombre = "Decano"
        cargo.id = 1
        cargo.puntos = 100
        return cargo
    
    def __assertCargo(self, cargo):
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.categoria_cargo)
        self.assertEqual(cargo.categoria_cargo.nombre, "Categoria 1")
        self.assertEqual(cargo.nombre, "Decano")
        self.assertEqual(cargo.puntos, 100)
if __name__ == '__main__':
    unittest.main()








