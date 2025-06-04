from app import db
from app.models import TipoDedicacion

class TipoDedicacionRepository:
    """
    Clase de Repositorio para la entidad TipoDedicacion
    """
    @staticmethod
    def crear (tipo_dedicacion):
        db.session.add(tipo_dedicacion)
        db.session.commit()

    @staticmethod
    def buscar_por_id (id: int):
        return db.session.query(TipoDedicacion).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(TipoDedicacion).all()

    @staticmethod
    def actualizar_tipo_dedicacion(tipo_dedicacion)-> TipoDedicacion:
        tipo_dedicacion_existente = db.session.merge(tipo_dedicacion)
        if not tipo_dedicacion_existente:
            return None
        return tipo_dedicacion_existente

    @staticmethod
    def borrar_por_id(id:int) -> TipoDedicacion:
        tipo_dedicacion = db.session.query(TipoDedicacion).filter_by(id=id).first()
        if not tipo_dedicacion:
             return None
        db.session.delete(tipo_dedicacion)
        db.session.commit()
        return tipo_dedicacion
