import unittest
import os
from flask import current_app
from app import create_app
from app.models import TipoDedicacion
from app.services import TipoDedicacionService
from app import db

class TipoDedicacionTestCase(unittest.TestCase):
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
        
    def test_tipodedicacion_creation(self):
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre= "Simple"
        tipo_dedicacion.observacion = "Observacion 1"
        self.assertIsNotNone(tipo_dedicacion)
        self.assertEqual(tipo_dedicacion.nombre, "Simple")
        self.assertIsNotNone(tipo_dedicacion.observacion)
        self.assertEqual(tipo_dedicacion.observacion, "Observacion 1")

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
        
    def test_tipodedicacion_creation(self):
        tipo_dedicacion = self.__nuevoTipoDedicacion()
        self.assertIsNotNone(tipo_dedicacion)
        self.assertEqual(tipo_dedicacion.nombre, "Simple")
        self.assertEqual(tipo_dedicacion.observacion, "Observacion 1")

    def test_crear_tipo_dedicacion(self):
        tipo_dedicacion = self.__nuevoTipoDedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        self.assertIsNotNone(tipo_dedicacion.id)
        self.assertGreaterEqual(tipo_dedicacion.id, 1)
        self.assertEqual(tipo_dedicacion.nombre, "Simple")

    def test_buscar_tipo_dedicacion_por_id(self):
        tipo_dedicacion = self.__nuevoTipoDedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        resultado = TipoDedicacionService.buscar_por_id(tipo_dedicacion.id)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Simple")
        self.assertEqual(resultado.observacion, "Observacion 1")

    def test_buscar_todos_los_tipos_dedicacion(self):
        tipo1 = self.__nuevoTipoDedicacion()
        tipo2 = self.__nuevoTipoDedicacion()
        tipo2.nombre = "Exclusiva"
        TipoDedicacionService.crear_tipo_dedicacion(tipo1)
        TipoDedicacionService.crear_tipo_dedicacion(tipo2)
        resultados = TipoDedicacionService.buscar_todos()
        self.assertIsNotNone(resultados)
        self.assertEqual(len(resultados), 2)

    def test_actualizar_tipo_dedicacion(self):
        tipo_dedicacion = self.__nuevoTipoDedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        tipo_dedicacion.nombre = "Semi-exclusiva"
        tipo_dedicacion.observacion = "Nueva observacion"
        actualizado = TipoDedicacionService.actualizar_tipo_dedicacion(tipo_dedicacion.id, tipo_dedicacion)
        self.assertIsNotNone(actualizado)
        self.assertEqual(actualizado.nombre, "Semi-exclusiva")
        self.assertEqual(actualizado.observacion, "Nueva observacion")

    def test_borrar_tipo_dedicacion(self):
        tipo_dedicacion = self.__nuevoTipoDedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
        borrado = TipoDedicacionService.borrar_por_id(tipo_dedicacion.id)
        self.assertIsNotNone(borrado)
        resultado = TipoDedicacionService.buscar_por_id(tipo_dedicacion.id)
        self.assertIsNone(resultado)
    



    #metodo para instanciar una clase en cada test
    def __nuevoTipoDedicacion(self):
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre = "Simple"
        tipo_dedicacion.observacion = "Observacion 1"
        return tipo_dedicacion

        
if __name__ == '__main__':
    unittest.main()