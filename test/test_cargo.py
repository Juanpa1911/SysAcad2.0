import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo
from app.services.cargo_service import CargoService


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
        
    def test_crear_cargo(self):
        cargo = self.__nuevoCargo()
        CargoService.crear_cargo(cargo)
        self.__assertCargo(cargo)
        
    def test_buscar_por_id(self):
        cargo = self.__nuevoCargo()
        CargoService.crear_cargo(cargo)
        encontrado = CargoService.buscar_por_id(cargo.id)
        self.__assertCargo(encontrado)
        
    def test_buscar_todos(self):
        cargo1 = self.__nuevoCargo()
        cargo2 = self.__nuevoCargo2()
        CargoService.crear_cargo(cargo1)
        CargoService.crear_cargo(cargo2)
        cargos = CargoService.buscar_todos()
        self.assertIsNotNone(cargos)
        self.assertEqual(len(cargos), 2)
    
    def test_actualizar_cargo(self):
        cargo = self.__nuevoCargo()
        CargoService.crear_cargo(cargo)
        cargo.nombre = "Decano actualizado"
        cargo.puntos = 120
        CargoService.actualizar_cargo(cargo.id, cargo)
        encontrado = CargoService.buscar_por_id(cargo.id)
        self.assertNotEqual(encontrado.nombre, "Decano")
        self.assertNotEqual(encontrado.puntos, 100)
       
        
    def test_borrar_cargo(self):
        cargo = self.__nuevoCargo()
        CargoService.crear_cargo(cargo)
        CargoService.borrar_por_id(cargo.id)
        encontrado = CargoService.buscar_por_id(cargo.id)
        self.assertIsNone(encontrado)
        
        
        
        
    def __nuevoCargo(self):
        cargo = Cargo()
        cargo.categoria_cargo = CategoriaCargo(nombre="Categoria 1")
        cargo.nombre = "Decano"
        cargo.id = 1
        cargo.puntos = 100
        return cargo
    
    def __nuevoCargo2(self):
        cargo = Cargo()
        cargo.categoria_cargo = CategoriaCargo(nombre="Categoria 2")
        cargo.nombre = "Vicedecano"
        cargo.id = 2
        cargo.puntos = 80
        return cargo
    
    def __assertCargo(self, cargo,):
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.categoria_cargo)
        self.assertEqual(cargo.categoria_cargo.nombre, "Categoria 1")
        self.assertEqual(cargo.nombre, "Decano")
        self.assertEqual(cargo.puntos, 100)
if __name__ == '__main__':
    unittest.main()








