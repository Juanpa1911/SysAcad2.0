import unittest
from datetime import date
from flask import current_app
from app import create_app, db
from app.models import Alumno, TipoDocumento
from app.services.alumno_service import AlumnoService
import os

class AlumnoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.tipo_documento = TipoDocumento(nombre="DNI")
        db.session.add(self.tipo_documento)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def __nuevoAlumno(self):
        return Alumno(
            apellido="Pérez",
            nombre="Juan",
            nro_documento="30123456",
            tipo_documento=self.tipo_documento,
            fecha_nacimiento="1990-01-15",
            sexo="M",
            nro_legajo=12345,
            fecha_ingreso=date.today()
        )
    
    def test_alumno_creation(self):
        alumno = self.__nuevoAlumno()
        self.assertIsNotNone(alumno)
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.nro_documento, "30123456")
        self.assertEqual(alumno.tipo_documento.nombre, "DNI")
        self.assertEqual(alumno.sexo, "M")
        self.assertEqual(alumno.nro_legajo, 12345)
    
    def test_crear_alumno(self):
        alumno = self.__nuevoAlumno()
        AlumnoService.crear_alumno(alumno)
        self.assertIsNotNone(alumno.id)
        alumno_db = AlumnoService.buscar_alumno_id(alumno.id)
        self.assertEqual(alumno_db.apellido, alumno.apellido)
        self.assertEqual(alumno_db.nro_legajo, alumno.nro_legajo)
    
    def test_actualizar_alumno(self):
        alumno = self.__nuevoAlumno()
        AlumnoService.crear_alumno(alumno)
        alumno.apellido = "González"
        alumno.nro_legajo = 54321
        AlumnoService.actualizar_alumno(alumno)
        alumno_actualizado = AlumnoService.buscar_alumno_id(alumno.id)
        self.assertEqual(alumno_actualizado.apellido, "González")
        self.assertEqual(alumno_actualizado.nro_legajo, 54321)
    
    def test_eliminar_alumno(self):
        alumno = self.__nuevoAlumno()
        AlumnoService.crear_alumno(alumno)
        alumno_id = alumno.id
        AlumnoService.borrar_alumno_id(alumno_id)
        alumno_eliminado = AlumnoService.buscar_alumno_id(alumno_id)
        self.assertIsNone(alumno_eliminado)
    
    def test_buscar_por_legajo(self):
        alumno = self.__nuevoAlumno()
        AlumnoService.crear_alumno(alumno)
        alumno_encontrado = AlumnoService.buscar_alumno_legajo(alumno.nro_legajo)
        self.assertIsNotNone(alumno_encontrado)
        self.assertEqual(alumno_encontrado.nro_documento, alumno.nro_documento)