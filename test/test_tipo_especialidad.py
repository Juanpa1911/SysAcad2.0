import os
import unittest
from flask import current_app
from app import db
from app import create_app
from app.models import TipoEspecialidad
from app.services import TipoEspecialidadService
from test.base_test import BaseTestCase
from test.instancias import nuevoTipoEspecialidad

class TipoEspecialidadTestCase(BaseTestCase):

    def test_crear_tipo_especialidad(self):
        tipo_especialidad = nuevoTipoEspecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad.id)
        self.assertGreaterEqual(tipo_especialidad.id, 1)
        self.assertEqual(tipo_especialidad.nombre, "Técnica")
        self.assertEqual(tipo_especialidad.nivel, "Básico")  

    def test_tipo_especialidad_busqueda(self):
        tipo_especialidad = nuevoTipoEspecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
        encontrado = TipoEspecialidadService.buscar_por_id(tipo_especialidad.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Técnica")
        self.assertEqual(encontrado.nivel, "Básico") 

    def test_buscar_tipos_especialidad(self):
        tipo_especialidad1 = nuevoTipoEspecialidad()
        tipo_especialidad2 = nuevoTipoEspecialidad("Electrica", "Avanzado")
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad1)
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad2)
        tipos_especialidad = TipoEspecialidadService.buscar_todos()
        self.assertIsNotNone(tipos_especialidad)
        self.assertEqual(len(tipos_especialidad), 2)

    def test_actualizar_tipo_especialidad(self):
        tipo_especialidad = nuevoTipoEspecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
        tipo_especialidad.nombre = "Cardiología Avanzada"
        tipo_especialidad.nivel = "Avanzado"
        tipo_especialidad_actualizado = TipoEspecialidadService.actualizar_tipo_especialidad(tipo_especialidad.id, tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad_actualizado)

    def test_borrar_tipo_especialidad(self):
        tipo_especialidad = nuevoTipoEspecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)

        # Borrar y verificar que devuelve el objeto borrado
        borrado = TipoEspecialidadService.borrar_por_id(tipo_especialidad.id)
        self.assertIsNotNone(borrado)
        self.assertEqual(borrado.nombre, "Técnica")
        self.assertEqual(borrado.nivel, "Básico")

        # Verificar que ya no existe en la base
        tipo_especialidad_borrado = TipoEspecialidadService.buscar_por_id(tipo_especialidad.id)
        self.assertIsNone(tipo_especialidad_borrado)
    
    if __name__ == '__main__':
        unittest.main()

        



