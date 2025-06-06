import unittest
from flask import current_app
from app import create_app
from app.models import Orientacion
from app.services import OrientacionService
from app import db
import os
from metodosDePrueba import nuevoOrientacion, nuevoOrientacion2


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
    
    def test_orientacion_creation(self):
        orientacion = nuevoOrientacion()
        self.assertIsNotNone(orientacion)
        self.assertEqual(orientacion.nombre, "Orientacion1")
        self.assertIsNotNone(orientacion.nombre)

    # Metodos CRUD
    def test_crear_orientacion(self):
        orientacion = nuevoOrientacion()
        OrientacionService.crear_orientacion(orientacion)
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.id)
        self.assertGreaterEqual(orientacion.id, 1)
        self.assertEqual(orientacion.nombre, "Orientacion1")

    def test_orientacion_busqueda(self):
        orientacion = nuevoOrientacion()
        OrientacionService.crear_orientacion(orientacion)
        OrientacionService.buscar_por_id(orientacion.id)
        self.assertIsNotNone(orientacion)
        self.assertEqual(orientacion.nombre, "Orientacion1")
    
    def test_buscar_orientaciones(self):
        orientacion1 = nuevoOrientacion()
        orientacion2 = nuevoOrientacion2()
        OrientacionService.crear_orientacion(orientacion1)
        OrientacionService.crear_orientacion(orientacion2)
        orientaciones = OrientacionService.buscar_todos()
        self.assertIsNotNone(orientaciones)
        self.assertEqual(len(orientaciones), 2)
        
    def test_actualizar_orientacion(self):
        orientacion = nuevoOrientacion()
        OrientacionService.crear_orientacion(orientacion)
        orientacion.nombre = "Orientacion2"
        orientacion_actualizada = OrientacionService.actualizar_orientacion(orientacion.id, orientacion)
        self.assertEqual(orientacion_actualizada.nombre, "Orientacion2")

    def test_borrar_orientacion(self):
        orientacion = nuevoOrientacion()
        OrientacionService.crear_orientacion(orientacion)
        db.session.delete(orientacion)
        db.session.commit()
        orientacion_borrada = OrientacionService.buscar_por_id(orientacion.id)
        self.assertIsNone(orientacion_borrada)