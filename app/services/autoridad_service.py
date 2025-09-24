from app.models import Autoridad
from app.repositories.autoridad_repositorio import AutoridadRepository

class AutoridadService:
    @staticmethod
    def crear_autoridad(autoridad: Autoridad) -> Autoridad:
        return AutoridadRepository.crear(autoridad)
    
    @staticmethod
    def obtener_autoridad_por_id(id: int) -> Autoridad:
        return AutoridadRepository.buscar_por_id(id)
    
    @staticmethod
    def obtener_todas_las_autoridades() -> list[Autoridad]:
        return AutoridadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_autoridad(id: int, autoridad: Autoridad) -> Autoridad:
        autoridad_existente = AutoridadRepository.buscar_por_id(id)
        if not autoridad_existente:
            return None
        autoridad_existente.nombre = autoridad.nombre

        return AutoridadRepository.actualizar_autoridad(autoridad_existente)

    @staticmethod
    def borrar_autoridad_por_id(id: int) -> Autoridad:
        return AutoridadRepository.borrar_por_id(id)