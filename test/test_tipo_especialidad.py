import unittest
import os
from flask import current_app
from app import create_app
from app.models import TipoEspecialidad
from app.services import TipoEspecialidadService
from app import db

class TipoEspecialidadTestCase(unittest.TestCase):
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

    def test_tipo_especialidad_creation(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        self.assertIsNotNone(tipo_especialidad)
        self.assertEqual(tipo_especialidad.nombre, "Cardiología")
        self.assertEqual(tipo_especialidad.nivel, "Básico")

    def test_crear_tipo_especialidad(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad.id)
        self.assertGreaterEqual(tipo_especialidad.id, 1)
        self.assertEqual(tipo_especialidad.nombre, "Cardiología")
        self.assertEqual(tipo_especialidad.nivel, "Básico")  

    def test_tipo_especialidad_busqueda(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
        encontrado = TipoEspecialidadService.buscar_por_id(tipo_especialidad.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Cardiología")
        self.assertEqual(encontrado.nivel, "Básico") 

    def test_buscar_tipos_especialidad(self):
        tipo_especialidad1 = self.__nuevoTipoEspecialidad("Cardiología")
        tipo_especialidad2 = self.__nuevoTipoEspecialidad("Neurología")
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad1)
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad2)
        tipos_especialidad = TipoEspecialidadService.buscar_todos()
        self.assertIsNotNone(tipos_especialidad)
        self.assertEqual(len(tipos_especialidad), 2)

    def test_actualizar_tipo_especialidad(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
        tipo_especialidad.nombre = "Cardiología Avanzada"
        tipo_especialidad.nivel = "Avanzado"
        tipo_especialidad_actualizado = TipoEspecialidadService.actualizar_tipo_especialidad(tipo_especialidad.id, tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad_actualizado)

    def test_borrar_tipo_especialidad(self):
        tipo_especialidad = self.__nuevoTipoEspecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)

        # Borrar y verificar que devuelve el objeto borrado
        borrado = TipoEspecialidadService.borrar_por_id(tipo_especialidad.id)
        self.assertIsNotNone(borrado)
        self.assertEqual(borrado.nombre, "Cardiología")
        self.assertEqual(borrado.nivel, "Básico")

        # Verificar que ya no existe en la base
        tipo_especialidad_borrado = TipoEspecialidadService.buscar_por_id(tipo_especialidad.id)
        self.assertIsNone(tipo_especialidad_borrado)
       

    def __nuevoTipoEspecialidad(self, nombre="Cardiología"):
        tipo_especialidad = TipoEspecialidad()
        tipo_especialidad.nombre = nombre
        tipo_especialidad.nivel = "Básico"
        return tipo_especialidad
    
    if __name__ == '__main__':
        unittest.main()

        



