import os
import unittest
from flask import current_app
from app import db
from datetime import date
from app import create_app
from app.models.plan import Plan
from app.models.orientacion import Orientacion
from app.services.plan_service import PlanService
from app.services.orientacion_service import OrientacionService
from test.base_test import BaseTestCase
from test.instancias import nuevoPlan, nuevaOrientacion


class PlanTestCase(BaseTestCase):
        
    def test_crear_plan(self):
        plan = nuevoPlan()
        PlanService.crear_plan(plan)
        self.assertIsNotNone(plan)
        self.assertIsNotNone(plan.id)
        self.assertGreaterEqual(plan.id, 1)
        self.assertEqual(plan.nombre, "Plan 2023")
        self.assertEqual(plan.fecha_inicio, date(2023, 1, 1))
        self.assertEqual(plan.fecha_fin, date(2028, 12, 31))
        self.assertEqual(plan.observacion, "Plan de estudios 2023")


    def test_plan_busqueda(self):
        plan = nuevoPlan()
        PlanService.crear_plan(plan)
        plan_encontrado = PlanService.buscar_por_id(plan.id)
        self.assertIsNotNone(plan_encontrado)
        self.assertEqual(plan_encontrado.nombre, "Plan 2023")

    def test_buscar_planes(self):
        plan1 = nuevoPlan()
        plan2 = nuevoPlan("Plan 2024")
        PlanService.crear_plan(plan1)
        PlanService.crear_plan(plan2)
        planes = PlanService.buscar_todos()
        self.assertIsNotNone(planes)
        self.assertEqual(len(planes), 2)

    def test_actualizar_plan(self):
        plan = nuevoPlan()
        PlanService.crear_plan(plan)
        plan.nombre = "Plan Modificado"
        plan.observacion = "Observación actualizada"
        plan_actualizado = PlanService.actualizar_plan(plan.id, plan)
        self.assertEqual(plan_actualizado.nombre, "Plan Modificado")
        self.assertEqual(plan_actualizado.observacion, "Observación actualizada")

    def test_borrar_plan(self):
        plan = nuevoPlan()
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
        plan = nuevoPlan()
        plan.orientacion_id = orientacion.id
        PlanService.crear_plan(plan)

        # Verificar que la relación se guardó correctamente
        plan_encontrado = PlanService.buscar_por_id(plan.id)
        self.assertEqual(plan_encontrado.orientacion_id, orientacion.id)

if __name__ == "__main__":
    unittest.main()
