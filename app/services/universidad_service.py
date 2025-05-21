from app.models import Universidad
from app.repositories import UniversidadRepository

class UniversidadService:
    """
    Clase de servicio para manejar la lógica de negocio relacionada con las universidades.
    """
    
    @staticmethod
    def crear_universidad(universidad: Universidad):
        """
        Crea una nueva universidad en la base de datos.
        :param universidad: Objeto Universidad a crear.
        :return: Objeto Universidad creado.
        """
        return UniversidadRepository.crear_universidad(universidad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Universidad:
        """
        Busca una universidad por su ID.
        :param id: ID de la universidad a buscar.
        :return: Objeto Universidad encontrado o None si no se encuentra.
        """
        return UniversidadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Universidad]:
        """
        Busca todas las universidades en la base de datos.
        :return: Lista de objetos Universidad.
        """
        return UniversidadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_universidad(id: int, universidad: Universidad) -> Universidad:
        """
        Actualiza una universidad existente en la base de datos.
        :param id: ID de la universidad a actualizar.
        :param universidad: Objeto Universidad con los nuevos datos.
        :return: Objeto Universidad actualizado o None si no se encuentra.
        """
        universidad_existente = UniversidadRepository.buscar_por_id(id)
        if not universidad_existente:
            return None
        universidad_existente.nombre = universidad.nombre
        universidad_existente.sigla = universidad.sigla
        return universidad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        """
        Borra una universidad por su ID.
        :param id: ID de la universidad a borrar.
        :return: True si se borró correctamente, False si no se encontró.
        """
        universidad = UniversidadRepository.buscar_por_id(id)
        if not universidad:
            return None
        return universidad