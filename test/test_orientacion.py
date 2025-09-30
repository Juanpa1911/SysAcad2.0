import os
import unittest
from flask import current_app
from app import db
from app import create_app
from app.models import Orientacion
from app.services import OrientacionService
from test.base_test import BaseTestCase
from test.instancias import nuevaOrientacion


class AppTestCase(BaseTestCase):

    def test_crear_orientacion(self):
        orientacion = nuevaOrientacion()
        OrientacionService.crear_orientacion(orientacion)
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.id)
        self.assertIsNotNone(orientacion.nombre)
        self.assertGreaterEqual(orientacion.id, 1)
        self.assertEqual(orientacion.nombre, "Sistemas de Información")

    def test_orientacion_busqueda(self):
        orientacion = nuevaOrientacion()
        OrientacionService.crear_orientacion(orientacion)
        OrientacionService.buscar_por_id(orientacion.id)
        self.assertIsNotNone(orientacion)
        self.assertEqual(orientacion.nombre, "Sistemas de Información")

    def test_buscar_orientaciones(self):
        orientacion1 = nuevaOrientacion()
        orientacion2 = nuevaOrientacion("Redes y Telecomunicaciones")
        OrientacionService.crear_orientacion(orientacion1)
        OrientacionService.crear_orientacion(orientacion2)
        orientaciones = OrientacionService.buscar_todos()
        self.assertIsNotNone(orientaciones)
        self.assertEqual(len(orientaciones), 2)
        
    def test_actualizar_orientacion(self):
        orientacion = nuevaOrientacion()
        OrientacionService.crear_orientacion(orientacion)
        orientacion.nombre = "Orientacion2"
        orientacion_actualizada = OrientacionService.actualizar_orientacion(orientacion.id, orientacion)
        self.assertEqual(orientacion_actualizada.nombre, "Orientacion2")

    def test_borrar_orientacion(self):
        orientacion = nuevaOrientacion()
        OrientacionService.crear_orientacion(orientacion)
        db.session.delete(orientacion)
        db.session.commit()
        orientacion_borrada = OrientacionService.buscar_por_id(orientacion.id)
        self.assertIsNone(orientacion_borrada)