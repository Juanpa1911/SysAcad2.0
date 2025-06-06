import unittest
import os
from flask import current_app
from app import create_app, db
from app.services.cargo_service import CargoService
from app.models import Cargo, CategoriaCargo, TipoDedicacion
from test.metodosDePrueba import nuevoCargo, nuevoCargo2, nuevoCargo3, categoriaCargo, categoriaCargo2, categoriaCargo3, tipoDeCargo, tipoDeCargo2


class CargoTestCase(unittest.TestCase):
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

    def test_crear_cargo(self):
        cargo = nuevoCargo()
        CargoService.crear_cargo(cargo)
        self.__assertCargo(cargo, cargo)  # Compara consigo mismo

    def test_buscar_por_id(self):
        cargo_original = nuevoCargo3()
        CargoService.crear_cargo(cargo_original)
        encontrado = CargoService.buscar_por_id(cargo_original.id)
        # Compara con el original
        self.__assertCargo(encontrado, cargo_original)

    def test_buscar_todos(self):
        cargo1 = nuevoCargo()
        cargo2 = nuevoCargo2()
        CargoService.crear_cargo(cargo1)
        CargoService.crear_cargo(cargo2)
        cargos = CargoService.buscar_todos()
        self.assertIsNotNone(cargos)
        self.assertEqual(len(cargos), 2)

    def test_actualizar_cargo(self):
        cargo = nuevoCargo()
        CargoService.crear_cargo(cargo)
        cargo.nombre = "Decano actualizado"
        cargo.puntos = 120
        CargoService.actualizar_cargo(cargo.id, cargo)
        encontrado = CargoService.buscar_por_id(cargo.id)
        self.assertNotEqual(encontrado.nombre, "Decano")
        self.assertNotEqual(encontrado.puntos, 100)

    def test_borrar_cargo(self):
        cargo = nuevoCargo()
        CargoService.crear_cargo(cargo)
        CargoService.borrar_por_id(cargo.id)
        encontrado = CargoService.buscar_por_id(cargo.id)
        self.assertIsNone(encontrado)

    def __assertCargo(self, cargo, cargo_original=None):
        """
        Verifica que un cargo tenga datos válidos y coincida con el original si se proporciona
        """
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.id)
        self.assertIsNotNone(cargo.categoria_cargo)
        self.assertIsNotNone(cargo.tipo_dedicacion)

        if cargo_original:
            self.assertEqual(cargo.nombre, cargo_original.nombre)
            self.assertEqual(cargo.puntos, cargo_original.puntos)
            self.assertEqual(cargo.categoria_cargo.nombre,
                             cargo_original.categoria_cargo.nombre)
            self.assertEqual(cargo.tipo_dedicacion.nombre,
                             cargo_original.tipo_dedicacion.nombre)


if __name__ == '__main__':
    unittest.main()
