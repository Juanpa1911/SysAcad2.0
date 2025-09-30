import os
import unittest
from flask import current_app
from app import create_app, db
from app.models import TipoDocumento
from app.services.tipo_doc_service import TipoDocumentoService
from test.base_test import BaseTestCase
from test.instancias import nuevoTipoDocumento

class TipoDocTestCase(BaseTestCase):

    def test_crear_tipo_documento(self):
        tipo_doc = nuevoTipoDocumento()
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        tipo_doc_db = TipoDocumentoService.buscar_documento_id(tipo_doc.id)
        self.assertIsNotNone(tipo_doc_db)
        self.assertEqual(tipo_doc_db.nombre, tipo_doc.nombre)
        
    def test_buscar_todos(self):
        tipo_doc1 = nuevoTipoDocumento()
        tipo_doc2 = nuevoTipoDocumento("Pasaporte")
        TipoDocumentoService.crear_tipo_documento(tipo_doc1)
        TipoDocumentoService.crear_tipo_documento(tipo_doc2)
        tipos_docs = TipoDocumentoService.buscar_todos_doc()
        self.assertGreaterEqual(len(tipos_docs), 2)
        self.assertIn(tipo_doc1, tipos_docs)
        self.assertIn(tipo_doc2, tipos_docs)
        
    def test_buscar_documento_id(self):
        tipo_doc = nuevoTipoDocumento()
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        tipo_doc_db = TipoDocumentoService.buscar_documento_id(tipo_doc.id)
        self.assertIsNotNone(tipo_doc_db)
        self.assertEqual(tipo_doc_db.nombre, tipo_doc.nombre)
        
    def test_actualizar_tipo_documento(self):
        tipo_doc = nuevoTipoDocumento()
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        tipo_doc.nombre = "DNI Actualizado"
        TipoDocumentoService.actualizar_tipo_documento(tipo_doc)
        tipo_doc_db = TipoDocumentoService.buscar_documento_id(tipo_doc.id)
        self.assertEqual(tipo_doc_db.nombre, "DNI Actualizado")
        
    def test_borrar_tipo_documento(self):
        tipo_doc = nuevoTipoDocumento()
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        TipoDocumentoService.borrar_tipo_documento_id(tipo_doc.id)
        tipo_doc_db = TipoDocumentoService.buscar_documento_id(tipo_doc.id)
        self.assertIsNone(tipo_doc_db)
        
    