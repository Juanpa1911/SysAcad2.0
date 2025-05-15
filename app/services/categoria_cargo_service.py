from app.models import CategoriaCargo
from app.repositories import CategoriaCargoRepository

class CategoriaCargoService:
    """
    Clase de servicio para la entidad CategoriaCargo.
    """
    @staticmethod
    def crear_categoria_cargo(categoria_cargo: CategoriaCargo):
        CategoriaCargoRepository.crear(categoria_cargo)
    
    @staticmethod
    def buscar_por_id(id: int) -> CategoriaCargo:
        return CategoriaCargoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[CategoriaCargo]:
        return CategoriaCargoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_categoria_cargo(id: int, categoria_cargo: CategoriaCargo) -> CategoriaCargo:
        categoria_cargo_existente = CategoriaCargoRepository.buscar_por_id(id)
        if not categoria_cargo_existente:
            return None
        categoria_cargo_existente.nombre = categoria_cargo.nombre
        return categoria_cargo_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> CategoriaCargo:
        categoria_cargo = CategoriaCargoRepository.borrar_por_id(id)
        if not categoria_cargo:
            return None
        return categoria_cargo