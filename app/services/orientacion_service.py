from app.models import Orientacion
from app.repositories.orientacion_repositorio import OrientacionRepository

class OrientacionService:
    """
    Clase de servicio para la entidad Orientacion.
    """
    @staticmethod
    def crear_orientacion(orientacion: Orientacion):
        OrientacionRepository.crear(orientacion)
    
    @staticmethod
    def buscar_por_id(id: int) -> Orientacion:
        return OrientacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Orientacion]:
        return OrientacionRepository.buscar_todas()
    
    @staticmethod
    def actualizar_orientacion(id: int, orientacion: Orientacion) -> Orientacion:
        orientacion_existente = OrientacionRepository.buscar_por_id(id)
        if not orientacion_existente:
            return None
        orientacion_existente.nombre = orientacion.nombre
        return orientacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Orientacion:
        orientacion = OrientacionRepository.borrar_por_id(id)
        if not orientacion:
            return None
        return orientacion
