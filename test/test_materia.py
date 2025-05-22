import unittest
from flask import current_app
from app import create_app, db
from app.models.materia import Materia
from app.models.orientacion import Orientacion
from app.services import MateriaService
import os


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

    def test_materia_creation(self):
        materia = self.__nuevoMateria()
        db.session.add(materia)
        db.session.commit()
        self._assert_materia(materia, "Matematica",
                             "MAT101", "Matematica basica")

    def test_crear_materia(self):
        materia = self.__nuevoMateria()
        MateriaService.crear_materia(materia)
        self._assert_materia(materia, "Matematica",
                             "MAT101", "Matematica basica")

    def test_buscar_por_id(self):
        materia = self.__nuevoMateria()
        MateriaService.crear_materia(materia)
        encontrado = MateriaService.buscar_por_id(materia.idMateria)
        self._assert_materia(encontrado, "Matematica",
                             "MAT101", "Matematica basica")

    def test_buscar_todos(self):
        materia1 = self.__nuevoMateria()
        materia2 = self.__nuevaMateria2()
        MateriaService.crear_materia(materia1)
        MateriaService.crear_materia(materia2)
        materias = MateriaService.buscar_todos()
        self._assert_materia(
            materias[0], "Matematica", "MAT101", "Matematica basica")
        self._assert_materia(
            materias[1], "Base de datos", "BD101", "Base de datos basica")

    def test_actualizar_materia(self):
        materia = self.__nuevoMateria()
        MateriaService.crear_materia(materia)
        materia.nombre = "Matematica avanzada"
        materia.codigo = "MAT201"
        materia.observacion = "Matematica avanzada basica"
        MateriaService.actualizar_materia(materia.idMateria, materia)
        encontrado = MateriaService.buscar_por_id(materia.idMateria)
        self._assert_materia(encontrado, "Matematica avanzada",
                             "MAT201", "Matematica avanzada basica")

    def test_borrar_materia(self):
        materia = self.__nuevoMateria()
        MateriaService.crear_materia(materia)
        MateriaService.borrar_por_id(materia.idMateria)
        encontrado = MateriaService.buscar_por_id(materia.idMateria)
        self.assertIsNone(encontrado)

# metodos para crear objetos de prueba

    def __nuevoMateria(self):
        materia = Materia()
        materia.nombre = "Matematica"
        materia.codigo = "MAT101"
        materia.observacion = "Matematica basica"
        return materia

    def __nuevaMateria2(self):
        materia = Materia()
        materia.nombre = "Base de datos"
        materia.codigo = "BD101"
        materia.observacion = "Base de datos basica"
        return materia

    def _assert_materia(self, materia, nombre, codigo, observacion):
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, nombre)
        self.assertEqual(materia.codigo, codigo)
        self.assertEqual(materia.observacion, observacion)
        self.assertIsNotNone(materia.idMateria)
        self.assertGreaterEqual(materia.idMateria, 1)
