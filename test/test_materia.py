import unittest
import os
from flask import current_app
from app import create_app, db
from app.models import Materia, Orientacion, Autoridad, Cargo, CategoriaCargo, TipoDedicacion
from app.services import MateriaService
from test.metodosDePrueba import nuevoMateria, nuevaMateria2, nuevoOrientacion, nuevaAutoridad

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


    def test_crear_materia(self):
        materia = nuevoMateria()
        MateriaService.crear_materia(materia)
        self._assert_materia(materia, "Matematica",
                             "MAT101", "Matematica basica")
        self.assertIsNotNone(materia.orientacion)
        self.assertIsNotNone(materia.autoridades)

    def test_buscar_por_id(self):
        materia = nuevoMateria()
        MateriaService.crear_materia(materia)
        encontrado = MateriaService.buscar_por_id(materia.id)
        self._assert_materia(encontrado, "Matematica","MAT101", "Matematica basica")
        self.assertIsNotNone(encontrado.orientacion)
        self.assertIsNotNone(encontrado.autoridades)

    def test_buscar_todos(self):
        materia1 = nuevoMateria()
        materia2 = nuevaMateria2()
        MateriaService.crear_materia(materia1)
        MateriaService.crear_materia(materia2)
        materias = MateriaService.buscar_todos()
        self._assert_materia(
            materias[0], "Matematica", "MAT101", "Matematica basica")
        self._assert_materia(
            materias[1], "Base de datos", "BD101", "Base de datos basica")
        self.assertEqual(len(materias), 2)
        
    def test_actualizar_materia(self):
        materia = nuevoMateria()
        MateriaService.crear_materia(materia)
        materia.nombre = "Matematica avanzada"
        materia.codigo = "MAT201"
        materia.observacion = "Matematica avanzada basica"
        MateriaService.actualizar_materia(materia.id, materia)
        encontrado = MateriaService.buscar_por_id(materia.id)
        self._assert_materia(encontrado, "Matematica avanzada",
                             "MAT201", "Matematica avanzada basica")

    def test_borrar_materia(self):
        materia = nuevoMateria()
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
