from app import db
from app.models import Departamento

class DepartamentoRepository:
    """
    clase de repositorio para la entidad Departamento.
    """
    @staticmethod
    def crear(departamento):
        db.session.add(departamento)
        db.session.commit()
    
    @staticmethod    
    def buscar_por_id(id: int):
        return db.session.query(Departamento).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        return db.session.query(Departamento).all()
    
    @staticmethod
    def actualizar_departamento(departamento) -> Departamento:
        db.session.merge(departamento)
        db.session.commit()
        return departamento
    
    @staticmethod
    def borrar_por_id(id: int) -> Departamento:
        departamento = db.session.query(Departamento).filter_by(id=id).first()
        if not departamento:
            return None
        db.session.delete(departamento)
        db.session.commit()
        return departamento
    