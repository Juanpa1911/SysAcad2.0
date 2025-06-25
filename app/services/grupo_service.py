from app.models import Grupo
from app.repositories.grupo_repositorio import GrupoRepository



class GrupoService:
    """
    Clase de servicio para la entidad Grupo.
    """
    @staticmethod
    def crear_grupo(grupo: Grupo):
        """
        Crea un nuevo grupo en la base de datos.
        :param grupo: Objeto Grupo
        :return: Objeto Grupo creado.
        """
        GrupoRepository.crear(grupo)
    
    @staticmethod
    def buscar_por_id(id: int) -> Grupo:
        """
        Busca un grupo por su ID.
        :param id: ID del grupo a buscar.
        :return: Objeto Grupo encontrado o None si no se encuentra.
        """
        return GrupoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Grupo]:
        """
        Busca todos los grupos en la base de datos.
        :return: Lista de objetos Grupo.
        """
        return GrupoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_grupo(id: int, grupo: Grupo) -> Grupo:
        """
        Actualiza un grupo existente en la base de datos.
        :param id: ID del grupo a actualizar.
        :param grupo: Objeto Grupo con los nuevos datos.
        :return: Objeto Grupo actualizado.
        """
        grupo_existente = GrupoRepository.buscar_por_id(id)
        if not grupo_existente:
            return None
        grupo_existente.nombre = grupo.nombre
        return grupo_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Grupo:
        """
        Borra un grupo por su ID.
        :param id: ID del grupo a borrar.
        :return: Objeto Grupo borrado o None si no se encuentra.
        """
        grupo = GrupoRepository.borrar_por_id(id)
        if not grupo:
            return None
        return grupo