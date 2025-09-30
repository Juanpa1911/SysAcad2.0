import unittest
import os
from flask import current_app
from app import db
from app import create_app
from app.models import Grado
from app.services import GradoService
from test.base_test import BaseTestCase
from test.instancias import nuevoGrado



class GradoTestCase(BaseTestCase):

    def test_crear_grado(self):
        grado = nuevoGrado()
        GradoService.crear_grado(grado)
        self.assertIsNotNone(grado)
        self.assertIsNotNone(grado.id)
        self.assertGreaterEqual(grado.id, 1)
        self.assertEqual(grado.nombre, "Licenciatura")

    def test_grado_busqueda(self):
        grado = nuevoGrado()
        GradoService.crear_grado(grado)
        grado_encontrado = GradoService.buscar_por_id(grado.id)
        self.assertIsNotNone(grado_encontrado)
        self.assertEqual(grado_encontrado.nombre, "Licenciatura")

    def test_buscar_grados(self):
        grado1 = nuevoGrado()
        grado2 = nuevoGrado("Maestría")
        GradoService.crear_grado(grado1)
        GradoService.crear_grado(grado2)
        grados = GradoService.buscar_todos()
        self.assertIsNotNone(grados)
        self.assertEqual(len(grados), 2)

    def test_actualizar_grado(self):
        grado = nuevoGrado()
        GradoService.crear_grado(grado)
        grado.nombre = "Doctorado"
        grado_actualizado = GradoService.actualizar_grado(grado.id, grado)
        self.assertEqual(grado_actualizado.nombre, "Doctorado")

    def test_borrar_grado(self):
        grado = nuevoGrado()
        GradoService.crear_grado(grado)
        resultado = GradoService.borrar_por_id(grado.id)
        self.assertTrue(resultado)
        grado_borrado = GradoService.buscar_por_id(grado.id)
        self.assertIsNone(grado_borrado)


if __name__ == "__main__":
    unittest.main()
