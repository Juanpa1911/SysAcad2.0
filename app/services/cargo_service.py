from app.models.autoridad import Cargo
from app.repositories.cargo_repositorio import CargoRepository

class CargoService:
    @staticmethod
    def crear_cargo(cargo: Cargo):
        CargoRepository.crear(cargo)
    
    @staticmethod
    def buscar_por_id(id: int) -> Cargo:
        return CargoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Cargo]:
        return CargoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_cargo(id: int, cargo: Cargo) -> Cargo:
        cargo_existente = CargoRepository.buscar_por_id(id)
        if not cargo_existente:
            return None
        cargo_existente.nombre = cargo.nombre
        cargo_existente.puntos = cargo.puntos
        return CargoRepository.actualizar_cargo(cargo_existente)
    
    @staticmethod
    def borrar_por_id(id: int) -> Cargo:
        return CargoRepository.borrar_por_id(id)