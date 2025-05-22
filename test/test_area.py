import unittest
from flask import current_app
from app import create_app
from app.models import Area
from app.services import AreaService
from app import db  
import os

class AppTestCase(unittest.TestCase):
    
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
    
    def test_area_creation(self):
        area = self.__nuevoArea()
        self.assertIsNotNone(area)
        self.assertEqual(area.nombre, "Area1")
        self.assertIsNotNone(area.nombre)
    
    #metdos crud
    def test_crear_area(self):
        area = self.__nuevoArea()
        AreaService.crear_area(area)
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.id)
        self.assertGreaterEqual(area.id, 1)
        self.assertEqual(area.nombre, "Area1")

    def test_area_busqueda(self):
        area = self.__nuevoArea()
        AreaService.crear_area(area)
        AreaService.buscar_por_id(area.id)
        self.assertIsNotNone(area)
        self.assertEqual(area.nombre, "Area1")
    
    def test_buscar_areas(self):
        area1 = self.__nuevoArea()
        area2 = self.__nuevoArea()
        AreaService.crear_area(area1)
        AreaService.crear_area(area2)
        areas = AreaService.buscar_todos()
        self.assertIsNotNone(areas)
        self.assertEqual(len(areas), 2)

    def test_actualizar_area(self):
        area = self.__nuevoArea()
        AreaService.crear_area(area)
        area.nombre = "Area2"
        area_actualizado = AreaService.actualizar_area(area.id, area)
        self.assertEqual(area_actualizado.nombre, "Area2")

    def test_borrar_area(self):
        area = self.__nuevoArea()
        AreaService.crear_area(area)
        db.session.delete(area)
        db.session.commit()
        area_borrada = AreaService.buscar_por_id(area.id)
        self.assertIsNone(area_borrada)



    def __nuevoArea(self):
        area = Area()
        area.nombre = "Area1"
        return area
    
if __name__ == '__main__':
    unittest.main()