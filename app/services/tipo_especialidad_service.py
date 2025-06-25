from app.models.tipo_especialidad import TipoEspecialidad
from app.repositories.tipo_especialidad_repositorio import TipoEspecialidadRepository


class TipoEspecialidadService:
    
    """Clase de servicio para la entidad Tipo Especialidad."""
    
    @staticmethod
    def crear_tipo_especialidad(tipo_especialidad: TipoEspecialidad):
        """
        Crea un nuevo tipo de especialidad en la base de datos.
        :param tipo_especialidad: Objeto TipoEspecialidad a crear.
        :return: Objeto TipoEspecialidad creado.
        """
        TipoEspecialidadRepository.crear(tipo_especialidad)

    @staticmethod
    def buscar_por_id(id: int) -> TipoEspecialidad:
        """        
        Busca un tipo de especialidad por su ID.
        :param id: ID del tipo de especialidad a buscar.
        :return: Objeto TipoEspecialidad encontrado o None si no se encuentra.
        """
        return TipoEspecialidadRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[TipoEspecialidad]:
        """
        Busca todos los tipos de especialidades en la base de datos.
        :return: Lista de objetos TipoEspecialidad.
        """
        return TipoEspecialidadRepository.buscar_todos()

    @staticmethod
    def actualizar_tipo_especialidad(id: int, tipo_especialidad: TipoEspecialidad) -> TipoEspecialidad:
        """
        Actualiza un tipo de especialidad existente en la base de datos.
        :param id: ID del tipo de especialidad a actualizar.
        :param tipo_especialidad: Objeto TipoEspecialidad con los nuevos datos.
        :return: Objeto TipoEspecialidad actualizado o None si no se encuentra.
        """
        tipo_especialidad_existente = TipoEspecialidadRepository.buscar_por_id(id)
        if not tipo_especialidad_existente:
            return None

        tipo_especialidad_existente.nombre = tipo_especialidad.nombre
        tipo_especialidad_existente.nivel = tipo_especialidad.nivel

        return TipoEspecialidadRepository.actualizar_tipo_especialidad(tipo_especialidad_existente)

    @staticmethod
    def borrar_por_id(id: int) -> TipoEspecialidad:
        """
        Borra un tipo de especialidad por su ID.
        :param id: ID del tipo de especialidad a borrar.
        :return: Objeto TipoEspecialidad borrado o None si no se encuentra.
        """
        return TipoEspecialidadRepository.borrar_por_id(id)

