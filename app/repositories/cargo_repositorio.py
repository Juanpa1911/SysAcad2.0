from app import db
from app.models.autoridad import Cargo

class CargoRepository:
    """"
    clase de repositorio para la entidad cargo.
    """
    @staticmethod
    def crear(cargo: Cargo):
        db.session.add(cargo)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int) -> Cargo:
        return db.session.query(Cargo).filter_by(id=id).first()

    @staticmethod
    def buscar_todos() -> list[Cargo]:
        return db.session.query(Cargo).all()

    @staticmethod
    def actualizar_cargo(cargo: Cargo) -> Cargo:
        cargo_existente = db.session.merge(cargo)
        if not cargo_existente:
            return None
        return cargo_existente

    @staticmethod
    def borrar_por_id(id: int) -> Cargo:
        cargo = db.session.query(Cargo).filter_by(id=id).first()
        if not cargo:
            return None
        db.session.delete(cargo)
        db.session.commit()
        return cargo