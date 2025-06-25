from app.models.plan import Plan
from app.repositories.plan_repositorio import PlanRepository


class PlanService:
    @staticmethod
    def crear_plan(plan: Plan):
        """
        Crea un nuevo plan en la base de datos.
        :param plan: Objeto Plan a crear.
        """
        PlanRepository.crear(plan)

    @staticmethod
    def buscar_por_id(id: int) -> Plan:
        """
        Busca un plan por su ID.
        :param id: ID del plan a buscar.
        :return: Objeto Plan encontrado o None si no se encuentra.
        """
        return PlanRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Plan]:
        """
        Busca todos los planes en la base de datos.
        :return: Lista de objetos Plan.
        """
        return PlanRepository.buscar_todos()

    @staticmethod
    def actualizar_plan(id: int, plan: Plan) -> Plan:
        """
        Actualiza un plan existente en la base de datos.
        :param id: ID del plan a actualizar.
        :param plan: Objeto Plan con los nuevos datos.
        :return: Objeto Plan actualizado o None si no se encuentra.
        """
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
        """
        Borra un plan por su ID.
        :param id: ID del plan a borrar.
        :return: Objeto Plan borrado o None si no se encuentra.
        """
        return PlanRepository.borrar_por_id(id)
