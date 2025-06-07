import unittest
import os 
from flask import current_app
from app import create_app, db
from app.models.especialidad import Especialidad
from app.services.especialidad_service import EspecialidadService
from app.repositories.especialidad_repositorio import EspecialidadRepository
from test.metodosDePrueba import nuevaEspecialidad, nuevaEspecialidad2


class EspecialidadTestCase (unittest.TestCase):

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


    def test_crear_especialidad(self):
        especialidad = nuevaEspecialidad()
        EspecialidadService.crear_especialidad(especialidad)
        self._assert_especialidad(especialidad, "Especialidad 1", "Observacion 1", "a")
        
    def test_buscar_por_id(self):
        especialidad = nuevaEspecialidad()
        EspecialidadService.crear_especialidad(especialidad)
        encontrada = EspecialidadService.buscar_por_id(especialidad.id)
        self._assert_especialidad(encontrada, "Especialidad 1", "Observacion 1", "a")

    def test_buscar_todos(self):
        especialidad1 = nuevaEspecialidad()
        especialidad2 = nuevaEspecialidad2()
        EspecialidadService.crear_especialidad(especialidad1)
        EspecialidadService.crear_especialidad(especialidad2)
        especialidades = EspecialidadService.buscar_todos()
        self.assertIsNotNone(especialidades)
        self.assertEqual(len(especialidades), 2)

    def test_actualizar_especialidad(self):
        especialidad = nuevaEspecialidad()
        EspecialidadService.crear_especialidad(especialidad)
        especialidad.nombre = "Especialidad Actualizada"
        especialidad.letra = "z"
        especialidad.observacion = "Observacion Actualizada"
        EspecialidadService.actualizar_especialidad(especialidad.id, especialidad)
        encontrada = EspecialidadService.buscar_por_id(especialidad.id)
        self._assert_especialidad(encontrada, "Especialidad Actualizada", "Observacion Actualizada", "z")

    def test_borrar_especialidad(self):
        especialidad = nuevaEspecialidad()
        EspecialidadService.crear_especialidad(especialidad)
        EspecialidadService.borrar_por_id(especialidad.id)
        encontrada = EspecialidadService.buscar_por_id(especialidad.id)
        self.assertIsNone(encontrada)

    #No repetir assert
    def _assert_especialidad(self, especialidad, nombre, observacion, letra):
        self.assertIsNotNone(especialidad)
        self.assertIsNotNone(especialidad.id)
        self.assertGreaterEqual(especialidad.id, 1)
        self.assertEqual(especialidad.nombre, nombre)
        self.assertEqual(especialidad.observacion, observacion)
        self.assertEqual(especialidad.letra, letra)



if __name__ == '__main__':
    unittest.main()