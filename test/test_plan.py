import unittest
import os
from flask import current_app
from app import create_app
from app.models.plan import Plan
from app.models.orientacion import Orientacion
from app.services.plan_service import PlanService
from app.services.orientacion_service import OrientacionService
from app import db


class PlanTestCase(unittest.TestCase):

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

    def test_plan_creation(self):
        plan = self.__nuevoPlan()
        self.assertIsNotNone(plan)
        self.assertEqual(plan.nombre, "Plan 2023")
        self.assertEqual(plan.fechaInicio, "2023-01-01")
        self.assertEqual(plan.fechaFin, "2027-12-31")
        self.assertEqual(plan.observacion, "Plan de estudios actualizado")

    def test_crear_plan(self):
        plan = self.__nuevoPlan()
        PlanService.crear_plan(plan)
        self.assertIsNotNone(plan)
        self.assertIsNotNone(plan.id)
        self.assertGreaterEqual(plan.id, 1)
        self.assertEqual(plan.nombre, "Plan 2023")

    def test_plan_busqueda(self):
        plan = self.__nuevoPlan()
        PlanService.crear_plan(plan)
        plan_encontrado = PlanService.buscar_por_id(plan.id)
        self.assertIsNotNone(plan_encontrado)
        self.assertEqual(plan_encontrado.nombre, "Plan 2023")

    def test_buscar_planes(self):
        plan1 = self.__nuevoPlan()
        plan2 = self.__nuevoPlan("Plan 2024")
        PlanService.crear_plan(plan1)
        PlanService.crear_plan(plan2)
        planes = PlanService.buscar_todos()
        self.assertIsNotNone(planes)
        self.assertEqual(len(planes), 2)

    def test_actualizar_plan(self):
        plan = self.__nuevoPlan()
        PlanService.crear_plan(plan)
        plan.nombre = "Plan Modificado"
        plan.observacion = "Observación actualizada"
        plan_actualizado = PlanService.actualizar_plan(plan.id, plan)
        self.assertEqual(plan_actualizado.nombre, "Plan Modificado")
        self.assertEqual(plan_actualizado.observacion,
                         "Observación actualizada")

    def test_borrar_plan(self):
        plan = self.__nuevoPlan()
        PlanService.crear_plan(plan)
        resultado = PlanService.borrar_por_id(plan.id)
        self.assertIsNotNone(resultado)
        plan_borrado = PlanService.buscar_por_id(plan.id)
        self.assertIsNone(plan_borrado)

    def test_plan_con_orientacion(self):
        # Crear una orientación
        orientacion = Orientacion()
        orientacion.nombre = "Orientación de Prueba"
        OrientacionService.crear_orientacion(orientacion)

        # Crear un plan asociado a la orientación
        plan = self.__nuevoPlan()
        plan.orientacion_id = orientacion.id
        PlanService.crear_plan(plan)

        # Verificar que la relación se guardó correctamente
        plan_encontrado = PlanService.buscar_por_id(plan.id)
        self.assertEqual(plan_encontrado.orientacion_id, orientacion.id)

    def __nuevoPlan(self, nombre="Plan 2023"):
        plan = Plan()
        plan.nombre = nombre
        plan.fechaInicio = "2023-01-01"
        plan.fechaFin = "2027-12-31"
        plan.observacion = "Plan de estudios actualizado"
        return plan


if __name__ == "__main__":
    unittest.main()
