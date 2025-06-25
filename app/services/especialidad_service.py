from app.models.especialidad import Especialidad
from app.repositories.especialidad_repositorio import EspecialidadRepository


class EspecialidadService:
    @staticmethod
    def crear_especialidad (especialidad: Especialidad):
        """ 
        Crea una nueva especialidad en la base de datos.
        :param especialidad: Objeto Especialidad a crear.
        :return: Objeto Especialidad creado.   
        """
        EspecialidadRepository.crear(especialidad)

    @staticmethod   
    def buscar_por_id (id: int) -> Especialidad:
        """
        Busca una especialidad por su ID.
        :param id: ID de la especialidad a buscar.  
        :return: Objeto Especialidad encontrado o None si no se encuentra.
        """
        return EspecialidadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Especialidad]:
        """
        Busca todas las especialidades en la base de datos.
        :return: Lista de objetos Especialidad.
        """
        return EspecialidadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_especialidad (id:int, especialidad: Especialidad) -> Especialidad:
        """
        Actualiza una especialidad existente en la base de datos.
        :param id: ID de la especialidad a actualizar.
        :param especialidad: Objeto Especialidad con los nuevos datos.
        :return: Objeto Especialidad actualizado o None si no se encuentra.
        """
        especialidad_existente = EspecialidadRepository.buscar_por_id(id)
        if not especialidad_existente:
            return None
        especialidad_existente.nombre = especialidad.nombre
        especialidad_existente.letra = especialidad.letra
        especialidad_existente.observacion = especialidad.observacion

        #actualizamos en DB llamando a repositorio
        return EspecialidadRepository.actualizar_especialidad (especialidad_existente)
    
    @staticmethod
    def borrar_por_id(id: int):
        """
        Borra una especialidad por su ID.
        :param id: ID de la especialidad a borrar.
        :return: True si se borró correctamente, False si no se encontró.
        """
        return EspecialidadRepository.borrar_por_id(id)
