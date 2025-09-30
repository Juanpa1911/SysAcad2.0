import unittest
from flask import current_app
from app.models import Universidad, Facultad
from app.services import UniversidadService
from test.base_test import BaseTestCase
from test.instancias import nuevaUniversidad
import os

class UniversidadTestCase(BaseTestCase):
        
    def test_crear_universidad(self):
        universidad = nuevaUniversidad()
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad.id, 1)
        self.assertIsNotNone(universidad.nombre)
        self.assertIsNotNone(universidad.sigla)
        
    def test_universidad_busqueda(self):
        universidad = nuevaUniversidad()
        res = UniversidadService.buscar_por_id(universidad.id)
        self.assertIsNotNone(res)
        self.assertIsNotNone(res.nombre)
        self.assertIsNotNone(res.sigla)
    
    def test_buscar_universidades(self):
        universidad1 = nuevaUniversidad()
        universidad2 = nuevaUniversidad()
        UniversidadService.crear_universidad(universidad1)
        UniversidadService.crear_universidad(universidad2)
        universidades = UniversidadService.buscar_todos()
        self.assertIsNotNone(universidades)
        self.assertEqual(len(universidades), 2)
        
    def test_actualizar_universidad(self):
        universidad = nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        universidad.nombre = "Universidad Nacional de Buenos Aires"
        universidad_actualizada = UniversidadService.actualizar_universidad(universidad.id, universidad)
        self.assertEqual(universidad_actualizada.nombre, "Universidad Nacional de Buenos Aires")
        
    def test_borrar_universidad(self):
        universidad = nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        borrado = UniversidadService.borrar_por_id(universidad.id)
        self.assertTrue(borrado)
        universidad_borrada = UniversidadService.buscar_por_id(universidad.id)
        self.assertIsNone(universidad_borrada)
    
if __name__ == '__main__':
    unittest.main()

