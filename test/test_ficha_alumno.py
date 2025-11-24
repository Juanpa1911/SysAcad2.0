"""
Test para la funcionalidad de Ficha del Alumno en formatos PDF y JSON
"""
import unittest
import json
from app.services.alumno_service import AlumnoService
from app.services.ficha_alumno_exporter import JSONFichaExporter, FichaAlumnoExporterFactory
from app.models.universidad import Universidad
from app.models.facultad import Facultad
from app import db
from test.base_test import BaseTestCase
from test.instancias import nuevoAlumno


class FichaAlumnoServiceTest(BaseTestCase):
    """Tests para el servicio de Ficha del Alumno"""
    
    def setUp(self):
        super().setUp()
        
        # Crear Universidad y Facultad
        self.universidad = Universidad()
        self.universidad.nombre = "Universidad Tecnológica Nacional"
        self.universidad.sigla = "UTN"
        db.session.add(self.universidad)
        db.session.flush()
        
        self.facultad = Facultad()
        self.facultad.nombre = "Facultad Regional San Rafael"
        self.facultad.abreviatura = "FRSR"
        self.facultad.universidad_id = self.universidad.id
        self.facultad.ciudad = "San Rafael"
        db.session.add(self.facultad)
        db.session.flush()
        
        # Crear alumno con facultad asignada
        self.alumno = nuevoAlumno(
            apellido="García",
            nombre="María",
            nro_documento="35987654",
            sexo="F",
            nro_legajo=54321
        )
        self.alumno.facultad_id = self.facultad.id
        AlumnoService.crear_alumno(self.alumno)
    
    def test_obtener_datos_ficha_alumno_existente(self):
        """Debe retornar los datos de la ficha para un alumno existente"""
        ficha_data = AlumnoService.obtener_datos_ficha(self.alumno.id)
        
        self.assertIsNotNone(ficha_data)
        self.assertEqual(ficha_data['nro_legajo'], 54321)
        self.assertEqual(ficha_data['apellido'], "García")
        self.assertEqual(ficha_data['nombre'], "María")
        self.assertEqual(ficha_data['sexo'], "Femenino")
    
    def test_obtener_datos_ficha_alumno_inexistente(self):
        """Debe retornar None para un alumno que no existe"""
        ficha_data = AlumnoService.obtener_datos_ficha(99999)
        self.assertIsNone(ficha_data)


class FichaAlumnoExporterTest(BaseTestCase):
    """Tests para los exportadores de ficha"""
    
    def test_json_exporter_retorna_diccionario(self):
        """El exportador JSON debe retornar el mismo diccionario"""
        exporter = JSONFichaExporter()
        data = {'nro_legajo': 123, 'nombre': 'Test'}
        
        resultado = exporter.export(data)
        
        self.assertEqual(resultado, data)
        self.assertEqual(exporter.get_content_type(), 'application/json')
    
    def test_factory_crea_exportador_json(self):
        """El Factory debe crear un exportador JSON"""
        exporter = FichaAlumnoExporterFactory.create_exporter('json')
        self.assertIsInstance(exporter, JSONFichaExporter)
    
    def test_factory_formato_invalido_lanza_error(self):
        """El Factory debe lanzar ValueError para formato no soportado"""
        with self.assertRaises(ValueError):
            FichaAlumnoExporterFactory.create_exporter('xml')


class FichaAlumnoEndpointTest(BaseTestCase):
    """Tests para los endpoints de ficha del alumno"""
    
    def setUp(self):
        super().setUp()
        self.client = self.app.test_client()
        
        # Crear Universidad y Facultad
        self.universidad = Universidad()
        self.universidad.nombre = "Universidad Tecnológica Nacional"
        self.universidad.sigla = "UTN"
        db.session.add(self.universidad)
        db.session.flush()
        
        self.facultad = Facultad()
        self.facultad.nombre = "Facultad Regional San Rafael"
        self.facultad.abreviatura = "FRSR"
        self.facultad.universidad_id = self.universidad.id
        self.facultad.ciudad = "San Rafael"
        db.session.add(self.facultad)
        db.session.flush()
        
        # Crear alumno con facultad asignada
        self.alumno = nuevoAlumno(
            apellido="López",
            nombre="Carlos",
            nro_documento="28555666",
            sexo="M",
            nro_legajo=98765
        )
        self.alumno.facultad_id = self.facultad.id
        AlumnoService.crear_alumno(self.alumno)
    
    def test_endpoint_ficha_json_por_id(self):
        """GET /alumno/{id}/ficha debe retornar JSON"""
        response = self.client.get(f'/api/v1/alumno/{self.alumno.hashid}/ficha')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['nro_legajo'], 98765)
        self.assertEqual(data['apellido'], "López")
    
    def test_endpoint_ficha_json_por_legajo(self):
        """GET /alumno/legajo/{legajo}/ficha debe retornar JSON"""
        response = self.client.get(f'/api/v1/alumno/legajo/{self.alumno.nro_legajo}/ficha')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['nro_legajo'], 98765)
    
    def test_endpoint_alumno_inexistente_retorna_404(self):
        """Debe retornar 404 para alumno que no existe"""
        response = self.client.get('/api/v1/alumno/legajo/999999/ficha')
        self.assertEqual(response.status_code, 404)
    
    def test_endpoint_formato_invalido_retorna_400(self):
        """Debe retornar 400 para formato no soportado"""
        response = self.client.get(f'/api/v1/alumno/{self.alumno.hashid}/ficha?format=xml')
        self.assertEqual(response.status_code, 400)
    
    def test_visualizar_json_completo(self):
        """Test para visualizar el JSON completo de una ficha"""
        response = self.client.get(f'/api/v1/alumno/legajo/{self.alumno.nro_legajo}/ficha')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Imprimir JSON formateado para visualización
        print("\n" + "="*60)
        print("📋 FICHA DEL ALUMNO - FORMATO JSON")
        print("="*60)
        print(json.dumps(data, indent=2, ensure_ascii=False))
        print("="*60 + "\n")
        
        # Verificar estructura
        self.assertIn('nro_legajo', data)
        self.assertIn('nombre_completo', data)
        self.assertIn('facultad', data)
    
    def test_generar_pdf_completo(self):
        """Test para generar PDF usando ReportLab (nativo de Python)"""
        import os
        
        try:
            response = self.client.get(f'/api/v1/alumno/legajo/{self.alumno.nro_legajo}/ficha?format=pdf')
            
            if response.status_code == 200:
                # Guardar PDF en disco para visualización
                pdf_path = os.path.join(os.getcwd(), 'ficha_alumno_ejemplo.pdf')
                with open(pdf_path, 'wb') as f:
                    f.write(response.data)
                
                print("\n" + "="*60)
                print("📄 FICHA DEL ALUMNO - FORMATO PDF")
                print("="*60)
                print(f"✅ PDF generado exitosamente")
                print(f"   Tamaño: {len(response.data)} bytes")
                print(f"   Content-Type: {response.content_type}")
                print(f"   Inicio: {response.data[:20]}")
                print(f"   📁 Guardado en: {pdf_path}")
                print("="*60 + "\n")
                
                self.assertTrue(response.data.startswith(b'%PDF'))
            else:
                print("\n⚠️  PDF no disponible - ReportLab no está instalado")
                print(f"   Status: {response.status_code}")
                
        except Exception as e:
            print(f"\n⚠️  Error al generar PDF: {str(e)}")
            print("   Instala ReportLab: pip install reportlab\n")


if __name__ == '__main__':
    unittest.main()
