from app.models import Materia
from app.repositories.materia_repositorio import MateriaRepository

class MateriaService:
    """
    Clase de servicio para la entidad Materia.
    """
    @staticmethod
    def crear_materia(materia: Materia):
        MateriaRepository.crear(materia)
    
    @staticmethod
    def buscar_por_id(id: int) -> Materia:
        return MateriaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Materia]:
        return MateriaRepository.buscar_todos()
    
    @staticmethod
    def actualizar_materia(id: int, materia: Materia) -> Materia:
        materia_existente = MateriaRepository.buscar_por_id(id)
        if not materia_existente:
            return None
        materia_existente.nombre = materia.nombre
        materia_existente.codigo = materia.codigo
        materia_existente.observacion = materia.observacion
        return materia_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Materia:
        materia = MateriaRepository.borrar_por_id(id)
        if not materia:
            return None
        return materia