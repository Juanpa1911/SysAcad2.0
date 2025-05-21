import unittest
from flask import current_app
from app import create_app, db
import os
from app.models.departamento import Departamento
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
        departamento = Departamento()
        departamento.nombre = "Secretaria"
        departamento.descripcion = "Secretaria de la empresa"
        db.session.add(departamento)
        db.session.commit()
        # Verificadores para la creación del departamento
        self.assertIsNotNone(departamento) 
        self.assertEqual(departamento.nombre, "Secretaria") 
        self.assertIsNotNone(departamento.nombre) # Verifica que el nombre no sea None
        # verificadores para la descripcion
        self.assertEqual(departamento.descripcion, "Secretaria de la empresa") # Verifica que la descripcion no sea None
        self.assertIsNotNone(departamento.descripcion) # Verifica que la descripcion no sea None
        # Verificadores para el id
        self.assertIsInstance(departamento.id, int)# Verifica que el id fue asignado automáticamente
        self.assertGreater(departamento.id, 0)
    
    def test_crear_departamento(self):
        departamento = Departamento()
        departamento.nombre = "ofina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        db.session.add(departamento)
        db.session.commit()
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.id)
        self.assertGreaterEqual(departamento.id, 1)
        self.assertEqual(departamento.nombre, "ofina de alumnos")
    
    def test_buscar_por_id(self):
        departamento = Departamento()
        departamento.nombre = "ofina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        db.session.add(departamento)
        db.session.commit()
        encontrado = Departamento.query.get(departamento.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "ofina de alumnos")

    def test_buscar_todos(self):
        departamento1 = Departamento()
        departamento1.nombre = "ofina de alumnos"
        departamento1.descripcion = "oficina de alumnos de la facultad de ingenieria"
        db.session.add(departamento1)
        
        departamento2 = Departamento()
        departamento2.nombre = "ofina de profesores"
        departamento2.descripcion = "oficina de profesores de la facultad de ingenieria"
        db.session.add(departamento2)
        
        db.session.commit()
        
        departamentos = Departamento.query.all()
        self.assertEqual(len(departamentos), 2)
        self.assertIn(departamento1, departamentos)
        self.assertIn(departamento2, departamentos)

    def test_actualizar_departamento(self):
        departamento = Departamento()
        departamento.nombre = "ofina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        db.session.add(departamento)
        db.session.commit()
        
        departamento.nombre = "oficina de alumnos"
        db.session.commit()
        
        actualizado = Departamento.query.get(departamento.id)
        self.assertEqual(actualizado.nombre, "oficina de alumnos")

    def test_borrar_departamento(self):
        departamento = Departamento()
        departamento.nombre = "ofina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        db.session.add(departamento)
        db.session.commit()
        
        db.session.delete(departamento)
        db.session.commit()
        
        encontrado = Departamento.query.get(departamento.id)
        self.assertIsNone(encontrado)
    
    def __nuevoDepartamento(self):
        departamento = Departamento()
        departamento.nombre = "ofina de alumnos"
        departamento.descripcion = "oficina de alumnos de la facultad de ingenieria"
        return departamento

    def __nuevoDepartamento2(self):
        departamento2 = Departamento()
        departamento2.nombre = "ofina de profesores"
        departamento2.descripcion = "oficina de profesores de la facultad de ingenieria"
        return departamento2
    
    def __nuevoDepartamento3(self):
        departamento3 = Departamento()
        departamento3.nombre = "ofina de administracion"
        departamento3.descripcion = "oficina de administracion de la facultad de ingenieria"
        return departamento3

if __name__ == '__main__':
    unittest.main()