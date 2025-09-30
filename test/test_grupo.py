import os
import unittest
from flask import current_app
from app import db
from app import create_app
from app.models import Grupo
from app.services import GrupoService
from test.base_test import BaseTestCase
from test.instancias import nuevoGrupo

class AppTestCase(BaseTestCase):

    def test_crear_grupo(self):
        grupo = nuevoGrupo()
        GrupoService.crear_grupo(grupo)
        self.assertIsNotNone(grupo)
        self.assertIsNotNone(grupo.id)
        self.assertGreaterEqual(grupo.id, 1)
        self.assertEqual(grupo.nombre, "Grupo A")
        
    def test_grupo_busqueda(self):
        grupo = nuevoGrupo()
        GrupoService.crear_grupo(grupo)
        GrupoService.buscar_por_id(grupo.id)
        self.assertIsNotNone(grupo)
        self.assertEqual(grupo.nombre, "Grupo A")
    
    def test_buscar_grupos(self):
        grupo1 = nuevoGrupo()
        grupo2 = nuevoGrupo()
        GrupoService.crear_grupo(grupo1)
        GrupoService.crear_grupo(grupo2)
        grupos = GrupoService.buscar_todos()
        self.assertIsNotNone(grupos)
        self.assertEqual(len(grupos), 2)
        
    def test_actualizar_grupo(self):
        grupo = nuevoGrupo()
        GrupoService.crear_grupo(grupo)
        grupo.nombre = "Grupo2"
        grupo_actualizado = GrupoService.actualizar_grupo(grupo.id, grupo)
        self.assertEqual(grupo_actualizado.nombre, "Grupo2")
        
    def test_borrar_grupo(self):
        grupo = nuevoGrupo()
        GrupoService.crear_grupo(grupo)
        db.session.delete(grupo)
        db.session.commit()
        grupo_borrado = GrupoService.borrar_por_id(grupo.id)
        self.assertIsNone(grupo_borrado)
    
if __name__ == '__main__':
    unittest.main()