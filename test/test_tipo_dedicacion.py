import os
import unittest
from flask import current_app
from app import db
from app import create_app
from app.models import TipoDedicacion
from app.services import TipoDedicacionService
from test.base_test import BaseTestCase
from test.instancias import nuevaTipoDedicacion

class TipoDedicacionTestCase(BaseTestCase):

    def test_crear_tipo_dedicacion(self):
        tipo_dedicacion = nuevaTipoDedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        self.assertIsNotNone(tipo_dedicacion.id)
        self.assertGreaterEqual(tipo_dedicacion.id, 1)
        self.assertIsNotNone(tipo_dedicacion)
        self.assertEqual(tipo_dedicacion.nombre, "Parcial")
        self.assertIsNotNone(tipo_dedicacion.observacion)
        self.assertEqual(tipo_dedicacion.observacion, "Dedicacion parcial")

    def test_buscar_tipo_dedicacion_por_id(self):
        tipo_dedicacion = nuevaTipoDedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        resultado = TipoDedicacionService.buscar_por_id(tipo_dedicacion.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Parcial")
        self.assertEqual(resultado.observacion, "Dedicacion parcial")

    def test_buscar_todos_los_tipos_dedicacion(self):
        tipo1 = nuevaTipoDedicacion()
        tipo2 = nuevaTipoDedicacion("Completa", "Dedicacion completa")
        TipoDedicacionService.crear_tipo_dedicacion(tipo1)
        TipoDedicacionService.crear_tipo_dedicacion(tipo2)
        resultados = TipoDedicacionService.buscar_todos()
        self.assertIsNotNone(resultados)
        self.assertEqual(len(resultados), 2)

    def test_actualizar_tipo_dedicacion(self):
        tipo_dedicacion = nuevaTipoDedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        tipo_dedicacion.nombre = "Semi-exclusiva"
        tipo_dedicacion.observacion = "Nueva observacion"
        actualizado = TipoDedicacionService.actualizar_tipo_dedicacion(tipo_dedicacion.id, tipo_dedicacion)
        self.assertIsNotNone(actualizado)
        self.assertEqual(actualizado.nombre, "Semi-exclusiva")
        self.assertEqual(actualizado.observacion, "Nueva observacion")

    def test_borrar_tipo_dedicacion(self):
        tipo_dedicacion = nuevaTipoDedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        borrado = TipoDedicacionService.borrar_por_id(tipo_dedicacion.id)
        self.assertIsNotNone(borrado)
        resultado = TipoDedicacionService.buscar_por_id(tipo_dedicacion.id)
        self.assertIsNone(resultado)
        
if __name__ == '__main__':
    unittest.main()