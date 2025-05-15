from app import db
from app.models import CategoriaCargo

class CategoriaCargoRepository:
    """
    Clase de repositorio para la entidad CategoriaCargo.
    """
    @staticmethod
    def crear(categoria_cargo):
        db.session.add(categoria_cargo)
        db.session.commit()
        
    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(CategoriaCargo).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        return db.session.query(CategoriaCargo).all()
    
    @staticmethod
    def actualizar_categoria_cargo(categoria_cargo) -> CategoriaCargo:
        categoria_cargo_existente = db.session.merge(categoria_cargo)
        if not categoria_cargo_existente:
            return None
        return categoria_cargo_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> CategoriaCargo:
        categoria_cargo = db.session.query(CategoriaCargo).filter_by(id=id).first()
        if not categoria_cargo:
            return None
        db.session.delete(categoria_cargo)
        db.session.commit()
        return categoria_cargo