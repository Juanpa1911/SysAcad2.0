import unittest
from flask import current_app
from app import create_app
from app.models import Grupo
from app.services import GrupoService
from app import db
import os

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
    
    def test_grupo_creation(self):
        grupo = self.__nuevoGrupo()
        self.assertIsNotNone(grupo)
        self.assertEqual(grupo.nombre, "Grupo1")
        self.assertIsNotNone(grupo.nombre) 

    def test_crear_grupo(self):
        grupo = self.__nuevoGrupo()
        GrupoService.crear_grupo(grupo)
        self.assertIsNotNone(grupo)
        self.assertIsNotNone(grupo.id)
        self.assertGreaterEqual(grupo.id, 1)
        self.assertEqual(grupo.nombre, "Grupo1")
        
    def test_grupo_busqueda(self):
        grupo = self.__nuevoGrupo()
        GrupoService.crear_grupo(grupo)
        GrupoService.buscar_por_id(grupo.id)
        self.assertIsNotNone(grupo)
        self.assertEqual(grupo.nombre, "Grupo1")
    
    def test_buscar_grupos(self):
        grupo1 = self.__nuevoGrupo()
        grupo2 = self.__nuevoGrupo()
        GrupoService.crear_grupo(grupo1)
        GrupoService.crear_grupo(grupo2)
        grupos = GrupoService.buscar_todos()
        self.assertIsNotNone(grupos)
        self.assertEqual(len(grupos), 2)
        
    def test_actualizar_grupo(self):
        grupo = self.__nuevoGrupo()
        GrupoService.crear_grupo(grupo)
        grupo.nombre = "Grupo2"
        grupo_actualizado = GrupoService.actualizar_grupo(grupo.id, grupo)
        self.assertEqual(grupo_actualizado.nombre, "Grupo2")
        
    def test_borrar_grupo(self):
        grupo = self.__nuevoGrupo()
        GrupoService.crear_grupo(grupo)
        db.session.delete(grupo)
        db.session.commit()
        grupo_borrado = GrupoService.borrar_por_id(grupo.id)
        self.assertIsNone(grupo_borrado)

    def __nuevoGrupo(self):
        grupo = Grupo()
        grupo.nombre = "Grupo1"
        return grupo 
    
if __name__ == '__main__':
    unittest.main()