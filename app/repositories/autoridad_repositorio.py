from app import db
from app.models import Autoridad

class AutoridadRepository:
    """
    Clase de repositorio para la entidad Autoridad.
    """
    @staticmethod
    def crear(autoridad):
        db.session.add(autoridad)
        db.session.commit()
        return autoridad
        
    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Autoridad).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        return db.session.query(Autoridad).all()
    
    @staticmethod
    def actualizar_autoridad(autoridad) -> Autoridad:
        autoridad_existente = db.session.merge(autoridad)
        if not autoridad_existente:
            return None
        return autoridad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Autoridad:
        autoridad = db.session.query(Autoridad).filter_by(id=id).first()
        if not autoridad:
            return None
        db.session.delete(autoridad)
        db.session.commit()
        return autoridad