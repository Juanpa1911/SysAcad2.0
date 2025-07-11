from app import db 
from app.models import Area


class AreaRepository:
    """
    Clase de repositorio para la entidad Area.
    """
    @staticmethod
    def crear(area):
        db.session.add(area)
        db.session.commit()
        return area
        
    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Area).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        return db.session.query(Area).all()
    
    @staticmethod
    def actualizar_area(area) -> Area:
        area_existente = db.session.merge(area)
        if not area_existente:
            return None
        return area_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Area:
        area = db.session.query(Area).filter_by(id=id).first()
        if not area:
            return None
        db.session.delete(area)
        db.session.commit()
        return area