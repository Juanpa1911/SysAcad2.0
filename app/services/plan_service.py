from app.models.plan import Plan
from app.repositories.plan_repositorio import PlanRepository


class PlanService:
    @staticmethod
    def crear_plan(plan: Plan):
        PlanRepository.crear(plan)

    @staticmethod
    def buscar_por_id(id: int) -> Plan:
        return PlanRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Plan]:
        return PlanRepository.buscar_todos()

    @staticmethod
    def actualizar_plan(id: int, plan: Plan) -> Plan:
        plan_existente = PlanRepository.buscar_por_id(id)
        if not plan_existente:
            return None

        plan_existente.nombre = plan.nombre
        plan_existente.fechaInicio = plan.fechaInicio
        plan_existente.fechaFin = plan.fechaFin
        plan_existente.observacion = plan.observacion
        plan_existente.orientacion_id = plan.orientacion_id

        return PlanRepository.actualizar_plan(plan_existente)

    @staticmethod
    def borrar_por_id(id: int) -> Plan:
        return PlanRepository.borrar_por_id(id)
