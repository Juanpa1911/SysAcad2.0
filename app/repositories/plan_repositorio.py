from app import db
from app.models.plan import Plan


class PlanRepository:
    @staticmethod
    def crear(plan: Plan):
        db.session.add(plan)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Plan).filter_by(id=id).first()

    @staticmethod
    def buscar_todos() -> list[Plan]:
        return db.session.query(Plan).all()

    @staticmethod
    def actualizar_plan(plan: Plan) -> Plan:
        plan_existente = db.session.merge(plan)
        if not plan_existente:
            return None
        db.session.commit()
        return plan_existente

    @staticmethod
    def borrar_por_id(id: int) -> Plan:
        plan = db.session.query(Plan).filter_by(id=id).first()
        if not plan:
            return None
        db.session.delete(plan)
        db.session.commit()
        return plan
