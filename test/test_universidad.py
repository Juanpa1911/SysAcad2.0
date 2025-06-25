import unittest
from flask import current_app
from app import create_app
from app.models import Universidad
from app.services import UniversidadService
from app.models import Facultad
from app import db
import os

class UniversidadTestCase(unittest.TestCase):

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

    def test_universidad_creation(self):
        universidad = self.__nuevaUniversidad()
        self.assertIsNotNone(universidad)
        self.assertEqual(universidad.nombre, "Universidad Nacional de La Plata")
        self.assertEqual(universidad.sigla, "UNLP")
        self.assertIsNotNone(universidad.nombre)
        self.assertIsNotNone(universidad.sigla)
        
    def test_crear_universidad(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad.id, 1)
        self.assertEqual(universidad.nombre, "Universidad Nacional de La Plata")
        self.assertEqual(universidad.facultades.count(), 2)  # Verifica que haya 2 facultades asociadas
        
    def test_universidad_busqueda(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        UniversidadService.buscar_por_id(universidad.id)
        self.assertIsNotNone(universidad)
        self.assertEqual(universidad.nombre, "Universidad Nacional de La Plata")
        self.assertEqual(universidad.sigla, "UNLP")
    
    def test_buscar_universidades(self):
        universidad1 = self.__nuevaUniversidad()
        universidad2 = self.__nuevaUniversidad()
        UniversidadService.crear_universidad(universidad1)
        UniversidadService.crear_universidad(universidad2)
        universidades = UniversidadService.buscar_todos()
        self.assertIsNotNone(universidades)
        self.assertEqual(len(universidades), 2)
        
    def test_actualizar_universidad(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        universidad.nombre = "Universidad Nacional de Buenos Aires"
        universidad_actualizada = UniversidadService.actualizar_universidad(universidad.id, universidad)
        self.assertEqual(universidad_actualizada.nombre, "Universidad Nacional de Buenos Aires")
        
    def test_borrar_universidad(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        db.session.delete(universidad)
        db.session.commit()
        universidad_borrada = UniversidadService.borrar_por_id(universidad.id)
        self.assertIsNone(universidad_borrada)
        
    def __nuevaUniversidad(self):
        universidad=Universidad()
        universidad.nombre = "Universidad Nacional de La Plata"
        universidad.sigla = "UNLP"
       
        facultad1 = self.__nuevafacultad()
        facultad2 = self.__nuevafacultad2()
        
        universidad.asociar_facultad(facultad1)
        universidad.asociar_facultad(facultad2)
        
        return universidad
    
    
    def __nuevafacultad(self):
        facultad = Facultad()
        facultad.nombre = "Facultad de Ingenieria"
        facultad.abreviatura = "FI" #TODO # Valor obligatorio
        return facultad

    def __nuevafacultad2(self):
        facultad = Facultad()
        facultad.nombre = "Facultad de Ciencias Exactas"
        facultad.abreviatura = "FCE"  # Valor obligatorio
        return facultad
    
if __name__ == '__main__':
    unittest.main()

