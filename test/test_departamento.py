import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.departamento import Departamento
from app.repositories.departamento_repositorio import DepartamentoRepository
from app.services.departamento_service import DepartamentoService

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

    def test_departamento_creation(self):
        departamento = self.__nuevoDepartamento()
        db.session.add(departamento)
        db.session.commit()
        self._assert_departamento(departamento, "ofina de alumnos", "oficina de alumnos de la facultad de ingenieria")

    def test_crear_departamento(self):
        departamento = self.__nuevoDepartamento()
        DepartamentoService.crear_departamento(departamento)
        self.assertIsNotNone(departamento)
        
    def test_buscar_por_id(self):
        departamento = self.__nuevoDepartamento()
        DepartamentoService.crear_departamento(departamento)
        encontrado = DepartamentoService.buscar_por_id(departamento.id)
        self._assert_departamento(encontrado, "ofina de alumnos", "oficina de alumnos de la facultad de ingenieria")

    def test_buscar_todos(self):
        departamento1 = self.__nuevoDepartamento()
        departamento2 = self.__nuevoDepartamento2()
        DepartamentoService.crear_departamento(departamento1)
        DepartamentoService.crear_departamento(departamento2)
        departamentos = DepartamentoService.buscar_todos()
        self.assertIsNotNone(departamentos)
        self.assertEqual(len(departamentos), 2)

    def test_actualizar_departamento(self):
        departamento = self.__nuevoDepartamento()
        DepartamentoService.crear_departamento(departamento)
        departamento.nombre = "oficina de alumnos actualizada"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria actualizada"
        DepartamentoService.actualizar_departamento(departamento.id, departamento)
        encontrado = DepartamentoService.buscar_por_id(departamento.id)
        self._assert_departamento(encontrado, "oficina de alumnos actualizada", "oficina de alumnos de la facultad de ingenieria actualizada")

    def test_borrar_departamento(self):
        departamento = self.__nuevoDepartamento()
        DepartamentoService.crear_departamento(departamento)
        DepartamentoService.borrar_por_id(departamento.id)
        encontrado = DepartamentoService.buscar_por_id(departamento.id)
        self.assertIsNone(encontrado)
        
        
# metodo para crear un nuevo departamento y no repetir tanto codigo
    def __nuevoDepartamento(self):
        departamento = Departamento()
        departamento.nombre = "ofina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        return departamento
    
    def __nuevoDepartamento2(self):
        departamento = Departamento()
        departamento.nombre = "ofina de profesores"
        departamento.descripcion = "oficina de profesores de la facultad de ingenieria"
        return departamento

    #metodo para ver si el departamento fue creado y no repetir tantos asserts
    def _assert_departamento(self, departamento, nombre, descripcion):
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.id)
        self.assertGreaterEqual(departamento.id, 1)
        self.assertEqual(departamento.nombre, nombre)
        self.assertEqual(departamento.descripcion, descripcion)

if __name__ == '__main__':
    unittest.main()