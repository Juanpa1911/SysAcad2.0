from app.models import Orientacion
from app.repositories.orientacion_repositorio import OrientacionRepository

class OrientacionService:
    """
    Clase de servicio para la entidad Orientacion.
    """
    @staticmethod
    def crear_orientacion(orientacion: Orientacion):
        """
        Crea una nueva orientacion en la base de datos.
        :param orientacion: Objeto Orientacion a crear.
        """
        OrientacionRepository.crear(orientacion)
    
    @staticmethod
    def buscar_por_id(id: int) -> Orientacion:
        """
        Busca una orientacion por su ID.
        :param id: ID de la orientacion a buscar.
        :return: Objeto Orientacion encontrado o None si no se encuentra.
        """
        return OrientacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Orientacion]:
        """
        Busca todas las orientaciones en la base de datos.
        :return: Lista de objetos Orientacion.
        """
        return OrientacionRepository.buscar_todas()
    
    @staticmethod
    def actualizar_orientacion(id: int, orientacion: Orientacion) -> Orientacion:
        """
        Actualiza una orientacion existente en la base de datos.
        :param id: ID de la orientacion a actualizar.
        :param orientacion: Objeto Orientacion con los nuevos datos.
        :return: Objeto Orientacion actualizado.
        """
        orientacion_existente = OrientacionRepository.buscar_por_id(id)
        if not orientacion_existente:
            return None
        orientacion_existente.nombre = orientacion.nombre
        return orientacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Orientacion:
        """
        Borra una orientacion por su ID.
        :param id: ID de la orientacion a borrar.
        :return: Objeto Orientacion borrado o None si no se encuentra.
        """
        orientacion = OrientacionRepository.borrar_por_id(id)
        if not orientacion:
            return None
        return orientacion
