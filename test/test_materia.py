import unittest
import os
from flask import current_app
from app import create_app, db
from app.models import Materia, Orientacion, Autoridad, Cargo, CategoriaCargo, TipoDedicacion
from app.services import MateriaService
from test.base_test import BaseTestCase
from test.instancias import nuevaMateria, nuevaMateria2

class AppTestCase(BaseTestCase):

    def test_crear_materia(self):
        materia = nuevaMateria()
        MateriaService.crear_materia(materia)
        self._assert_materia(materia, "Analisis Matematico I", "ANMAT1", "Introducción al Análisis Matemático")
        self.assertIsNotNone(materia.orientacion)
        self.assertIsNotNone(materia.autoridades)

    def test_buscar_por_id(self):
        materia = nuevaMateria()
        MateriaService.crear_materia(materia)
        encontrado = MateriaService.buscar_por_id(materia.id)
        self._assert_materia(encontrado, "Analisis Matematico I", "ANMAT1", "Introducción al Análisis Matemático")
        self.assertIsNotNone(encontrado.orientacion)
        self.assertIsNotNone(encontrado.autoridades)

    def test_buscar_todos(self):
        materia1 = nuevaMateria()
        materia2 = nuevaMateria("Bases de Datos", "BD1", "Introducción a las Bases de Datos")
        MateriaService.crear_materia(materia1)
        MateriaService.crear_materia(materia2)
        materias = MateriaService.buscar_todos()
        self._assert_materia(materias[0], "Analisis Matematico I", "ANMAT1", "Introducción al Análisis Matemático")
        self._assert_materia(materias[1], "Bases de Datos", "BD1", "Introducción a las Bases de Datos")
        self.assertEqual(len(materias), 2)
        
    def test_actualizar_materia(self):
        materia = nuevaMateria()
        MateriaService.crear_materia(materia)
        materia.nombre = "Matematica avanzada"
        materia.codigo = "MAT201"
        materia.observacion = "Matematica avanzada basica"
        MateriaService.actualizar_materia(materia.id, materia)
        encontrado = MateriaService.buscar_por_id(materia.id)
        self._assert_materia(encontrado, "Matematica avanzada","MAT201", "Matematica avanzada basica")

    def test_borrar_materia(self):
        materia = nuevaMateria()
        MateriaService.crear_materia(materia)
        MateriaService.borrar_por_id(materia.id)
        encontrado = MateriaService.buscar_por_id(materia.id)
        self.assertIsNone(encontrado)
        
    def _assert_materia(self, materia, nombre, codigo, observacion):
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, nombre)
        self.assertEqual(materia.codigo, codigo)
        self.assertEqual(materia.observacion, observacion)
        self.assertIsNotNone(materia.id)
        self.assertGreaterEqual(materia.id, 1)
