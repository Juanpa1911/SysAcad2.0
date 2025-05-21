from app import db
from app.models import Orientacion

class OrientacionRepository:
    """
    Clase de repositorio para la entidad Orientacion.
    """
    @staticmethod
    def crear(orientacion: Orientacion):

        db.session.add(orientacion)
        db.session.commit()
        
    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Orientacion).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todas() -> list[Orientacion]:
        return db.session.query(Orientacion).all()
    
    @staticmethod
    def actualizar_orientacion(orientacion: Orientacion) -> Orientacion:
        orientacion_existente = db.session.merge(orientacion)
        if not orientacion_existente:
            return None
        return orientacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Orientacion:
        orientacion = db.session.query(Orientacion).filter_by(id=id).first()
        if not orientacion:
            return None
        db.session.delete(orientacion)
        db.session.commit()
        return orientacion
    