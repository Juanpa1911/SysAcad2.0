import os
import unittest
from flask import current_app
from app import create_app, db
from app.models import Facultad, Universidad
from app.services import FacultadService, UniversidadService
from test.base_test import BaseTestCase
from test.instancias import nuevaFacultad, nuevaUniversidad

class FacultadTestCase(BaseTestCase):

    def test_crear_facultad(self):
        universidad = nuevaUniversidad()
        facultad = nuevaFacultad()
        FacultadService.crear_facultad(facultad)
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.id)
        self.assertGreaterEqual(facultad.id, 1)
        self.assertEqual(facultad.nombre, "Facultad de Ingeniería")

    def test_buscar_facultad_por_id(self):
        universidad = nuevaUniversidad()
        facultad = nuevaFacultad()
        FacultadService.crear_facultad(facultad)
        facultad_encontrada = FacultadService.buscar_por_id(facultad.id)
        self.assertIsNotNone(facultad_encontrada)
        self.assertEqual(facultad_encontrada.nombre, "Facultad de Ingeniería")
        self.assertEqual(facultad.abreviatura, "FI")

    def test_buscar_facultades(self):
        universidad = nuevaUniversidad()
        facultad1 = nuevaFacultad()
        facultad2 = nuevaFacultad("Facultad de Ciencias", "FC", universidad.id)
        FacultadService.crear_facultad(facultad1)
        FacultadService.crear_facultad(facultad2)
        facultades = FacultadService.buscar_todos()
        self.assertIsNotNone(facultades)
        self.assertEqual(len(facultades), 2)

    def test_actualizar_facultad(self):
        universidad = nuevaUniversidad()
        facultad = nuevaFacultad()
        FacultadService.crear_facultad(facultad)
        facultad.nombre = "Facultad de Ciencias Naturales"
        facultad_actualizada = FacultadService.actualizar_facultad(facultad.id, facultad)
        self.assertEqual(facultad_actualizada.nombre, "Facultad de Ciencias Naturales")

    def test_borrar_facultad(self):
        universidad = nuevaUniversidad()
        facultad = nuevaFacultad()
        FacultadService.crear_facultad(facultad)
        db.session.delete(facultad)
        db.session.commit()
        facultad_borrada = FacultadService.borrar_por_id(facultad.id)
        self.assertIsNone(facultad_borrada)

if __name__ == "__main__":
    unittest.main()
