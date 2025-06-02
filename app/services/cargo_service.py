from app.models.autoridad import Cargo
from app.repositories.cargo_repositorio import CargoRepository

class CargoService:
    """
    Clase de servicio para la entidad Cargo.
    """
    
    @staticmethod
    def crear_cargo(cargo: Cargo):
        """
        Crea un nuevo cargo en la base de datos.
        :param cargo: Objeto Cargo a crear.
        :return: Objeto Cargo creado.
        """
        CargoRepository.crear(cargo)
    
    @staticmethod
    def buscar_por_id(id: int) -> Cargo:
        """
        Busca un cargo por su ID.
        :param id: ID del cargo a buscar.
        :return: Objeto Cargo encontrado o None si no se encuentra.
        """
        return CargoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Cargo]:
        """
        Busca todos los cargos en la base de datos.
        :return: Lista de objetos Cargo.
        """
        return CargoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_cargo(id: int, cargo: Cargo) -> Cargo:
        """
        Actualiza un cargo existente en la base de datos.
        :param id: ID del cargo a actualizar.
        :param cargo: Objeto Cargo con los nuevos datos.
        :return: Objeto Cargo actualizado o None si no se encuentra.
        """
        cargo_existente = CargoRepository.buscar_por_id(id)
        if not cargo_existente:
            return None
        cargo_existente.nombre = cargo.nombre
        cargo_existente.puntos = cargo.puntos
        return CargoRepository.actualizar_cargo(cargo_existente)
    
    @staticmethod
    def borrar_por_id(id: int) -> Cargo:
        """
        Borra un cargo por su ID.
        :param id: ID del cargo a borrar.
        :return: Objeto Cargo borrado o None si no se encuentra.
        """
        return CargoRepository.borrar_por_id(id)