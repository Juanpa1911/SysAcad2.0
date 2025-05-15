from app import db
from app.models import Grupo

class GrupoRepository:
    """
    Clase de repositorio para la entidad Grupo.
    """
    @staticmethod
    def crear(grupo):

        db.session.add(grupo)
        db.session.commit()
        
    @staticmethod
    def buscar_por_id(id: int):

        return db.session.query(Grupo).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        return db.session.query(Grupo).all()
    
    @staticmethod
    def actualizar_grupo(grupo) -> Grupo:
        grupo_existente = db.session.merge(grupo)
        if not grupo_existente:
            return None
        return grupo_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Grupo:

        grupo = db.session.query(Grupo).filter_by(id=id).first()
        if not grupo:
            return None
        db.session.delete(grupo)
        db.session.commit()
        return grupo
