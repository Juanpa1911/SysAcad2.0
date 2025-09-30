import os
import unittest
from flask import current_app
from app import db 
from app import create_app
from app.models import Area
from app.services import AreaService 
from test.base_test import BaseTestCase
from test.instancias import nuevaArea


class AppTestCase(BaseTestCase):
    
    def test_crear_area(self):
        area = nuevaArea()
        AreaService.crear_area(area)
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.id)
        self.assertGreaterEqual(area.id, 1)
        self.assertEqual(area.nombre, "Área de Investigación")

    def test_buscar_area_por_id(self):
        area = nuevaArea()
        AreaService.crear_area(area)
        area_encontrada = AreaService.buscar_por_id(area.id)
        self.assertIsNotNone(area_encontrada)
        self.assertEqual(area_encontrada.nombre, "Área de Investigación")
    
    def test_buscar_areas(self):
        area1 = nuevaArea()
        area2 = nuevaArea()
        AreaService.crear_area(area1)
        AreaService.crear_area(area2)
        areas = AreaService.buscar_todos()
        self.assertIsNotNone(areas)
        self.assertEqual(len(areas), 2)

    def test_actualizar_area(self):
        area = nuevaArea()
        AreaService.crear_area(area)
        area.nombre = "Area2"
        area_actualizado = AreaService.actualizar_area(area.id, area)
        self.assertEqual(area_actualizado.nombre, "Area2")

    def test_borrar_area(self):
        area = nuevaArea()
        AreaService.crear_area(area)
        db.session.delete(area)
        db.session.commit()
        area_borrada = AreaService.buscar_por_id(area.id)
        self.assertIsNone(area_borrada)
    
if __name__ == '__main__':
    unittest.main()