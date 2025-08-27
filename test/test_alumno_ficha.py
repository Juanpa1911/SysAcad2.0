import unittest
import os
from app import create_app, db
from app.models.alumno import Alumno
from app.models.facultad import Facultad
from app.services.alumno_service import AlumnoService

class AlumnoFichaTestCase(unittest.TestCase):
    
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()
        
        self.facultad = Facultad()
        self.facultad.nombre = "Facultad de Ingeniería"
        self.facultad.abreviatura = "FI"
        db.session.add(self.facultad)
        db.session.commit()
        
        self.alumno = Alumno()
        self.alumno.nro_legajo = "12345"
        self.alumno.apellido = "García"
        self.alumno.nombre = "Juan"
        db.session.add(self.alumno)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_obtener_ficha_json(self):
        response = self.client.get(f'/api/v1/alumno/{self.alumno.id}/ficha')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['legajo'], '12345')
        self.assertEqual(data['apellido'], 'García')
        self.assertEqual(data['facultad_nombre'], 'Facultad de Ingeniería')
    
    def test_obtener_ficha_pdf(self):
        response = self.client.get(f'/api/v1/alumno/{self.alumno.id}/ficha/pdf')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/pdf')

if __name__ == '__main__':
    unittest.main()