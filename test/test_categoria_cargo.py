import unittest
from flask import current_app
from app import create_app
from app.models import CategoriaCargo
from app.services import CategoriaCargoService
from app import db
import os

class CategoriaCargoTestCase(unittest.TestCase):
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
        
    def test_categoriacargo_creation(self):
        categoria_cargo = self.__nuevaCategoriaCargo()
        self.assertIsNotNone(categoria_cargo)
        self.assertEqual(categoria_cargo.nombre, "Categoria 1")

    def test_crear_categoria_cargo(self):
        categoria_cargo = self.__nuevaCategoriaCargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo)
        self.assertIsNotNone(categoria_cargo)
        self.assertIsNotNone(categoria_cargo.id)
        self.assertGreaterEqual(categoria_cargo.id, 1)
        self.assertEqual(categoria_cargo.nombre, "Categoria 1")

    def test_categoria_cargo_busqueda(self):
        categoria_cargo = self.__nuevaCategoriaCargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo)
        CategoriaCargoService.buscar_por_id(categoria_cargo.id)
        self.assertIsNotNone(categoria_cargo)
        self.assertEqual(categoria_cargo.nombre, "Categoria 1")

    def test_buscar_categorias_cargos(self):
        categoria_cargo1 = self.__nuevaCategoriaCargo()
        categoria_cargo2 = self.__nuevaCategoriaCargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo1)
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo2)
        categorias_cargos = CategoriaCargoService.buscar_todos()
        self.assertIsNotNone(categorias_cargos)
        self.assertEqual(len(categorias_cargos), 2)

    def test_actualizar_categoria_cargo(self):
        categoria_cargo = self.__nuevaCategoriaCargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo)
        categoria_cargo.nombre = "Categoria 2"
        categoria_cargo_actualizado = CategoriaCargoService.actualizar_categoria_cargo(categoria_cargo.id, categoria_cargo)
        self.assertEqual(categoria_cargo_actualizado.nombre, "Categoria 2")

    def test_borrar_categoria_cargo(self):
        categoria_cargo = self.__nuevaCategoriaCargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo)
        db.session.delete(categoria_cargo)
        db.session.commit()
        categoria_cargo_borrada = CategoriaCargoService.borrar_por_id(categoria_cargo.id)
        self.assertIsNone(categoria_cargo_borrada)
    
    def __nuevaCategoriaCargo(self):
        categoria_cargo = CategoriaCargo()
        categoria_cargo.nombre= "Categoria 1"
        return categoria_cargo
    
if __name__ == '__main__':
    unittest.main()