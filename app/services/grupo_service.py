from app.models import Grupo
from app.repositories.grupo_repositorio import GrupoRepository



class GrupoService:
    """
    Clase de servicio para la entidad Grupo.
    """
    @staticmethod
    def crear_grupo(grupo: Grupo):
        GrupoRepository.crear(grupo)
    
    @staticmethod
    def buscar_por_id(id: int) -> Grupo:
        return GrupoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Grupo]:

        return GrupoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_grupo(id: int, grupo: Grupo) -> Grupo:
        grupo_existente = GrupoRepository.buscar_por_id(id)
        if not grupo_existente:
            return None
        grupo_existente.nombre = grupo.nombre
        return grupo_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Grupo:

        grupo = GrupoRepository.buscar_por_id(id)
        if not grupo:
            return None
        return grupo