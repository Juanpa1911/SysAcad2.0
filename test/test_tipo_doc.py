import unittest
from flask import current_app
from app import create_app, db
import os
from app.models import TipoDocumento
from app.services.tipo_doc_service import TipoDocumentoService


class TipoDocTestCase(unittest.TestCase):
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

    def test_crear_tipo_documento(self):
        tipo_doc = TipoDocumento(nombre="DNI")
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        self.assertIsNotNone(tipo_doc.id)
        tipo_doc_db = TipoDocumentoService.buscar_documento_id(tipo_doc.id)
        self.assertEqual(tipo_doc_db.nombre, tipo_doc.nombre)
        
    def test_buscar_todos(self):
        tipo_doc1 = TipoDocumento(nombre="DNI")
        tipo_doc2 = TipoDocumento(nombre="Pasaporte")
        TipoDocumentoService.crear_tipo_documento(tipo_doc1)
        TipoDocumentoService.crear_tipo_documento(tipo_doc2)
        
        tipos_docs = TipoDocumentoService.buscar_todos_doc()
        self.assertGreaterEqual(len(tipos_docs), 2)
        self.assertIn(tipo_doc1, tipos_docs)
        self.assertIn(tipo_doc2, tipos_docs)
        
    def test_buscar_documento_id(self):
        tipo_doc = TipoDocumento(nombre="DNI")
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        tipo_doc_db = TipoDocumentoService.buscar_documento_id(tipo_doc.id)
        self.assertIsNotNone(tipo_doc_db)
        self.assertEqual(tipo_doc_db.nombre, tipo_doc.nombre)
        
    def test_actualizar_tipo_documento(self):
        tipo_doc = TipoDocumento(nombre="DNI")
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        tipo_doc.nombre = "DNI Actualizado"
        TipoDocumentoService.actualizar_tipo_documento(tipo_doc)
        
        tipo_doc_db = TipoDocumentoService.buscar_documento_id(tipo_doc.id)
        self.assertEqual(tipo_doc_db.nombre, "DNI Actualizado")
        
    def test_borrar_tipo_documento(self):
        tipo_doc = TipoDocumento(nombre="DNI")
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        TipoDocumentoService.borrar_tipo_documento_id(tipo_doc.id)
        
        tipo_doc_db = TipoDocumentoService.buscar_documento_id(tipo_doc.id)
        self.assertIsNone(tipo_doc_db)
        
    