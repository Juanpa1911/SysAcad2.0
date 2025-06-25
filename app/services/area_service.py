from app.models import Area
from app.repositories.area_repositorio import AreaRepository




class AreaService:
    """
    Clase servicio para la entidad de Area.
    """
    @staticmethod
    def crear_area(area: Area):
        """
        Crea un nuevo área en la base de datos.
        :param area: Objeto Area a crear.
        :return: Objeto Area creado.
        """
        AreaRepository.crear(area)
    
    @staticmethod
    def buscar_por_id(id: int) -> Area:
        """
        Busca un área por su ID.
        :param id: ID del área a buscar.
        :return: Objeto Area encontrado o None si no se encuentra.
        """
        return AreaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Area]:
        """
        Busca todas las áreas en la base de datos.
        :return: Lista de objetos Area.
        """
        return AreaRepository.buscar_todos()
    
    @staticmethod
    def actualizar_area(id: int, area: Area) -> Area:
        """
        Actualiza un área existente en la base de datos.
        :param id: ID del área a actualizar.
        :param area: Objeto Area con los nuevos datos.
        :return: Objeto Area actualizado o None si no se encuentra.
        """
        area_existente = AreaRepository.buscar_por_id(id)
        if not area_existente:
            return None
        area_existente.nombre = area.nombre
        return area_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Area:
        """
        Borra un área por su ID.
        :param id: ID del área a borrar.
        :return: Objeto Area borrado o None si no se encuentra.
        """
        area = AreaRepository.borrar_por_id(id)
        if not area:
            return None
        return area