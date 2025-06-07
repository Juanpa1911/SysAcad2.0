from app.models.tipo_especialidad import TipoEspecialidad
from app.repositories.tipo_especialidad_repositorio import TipoEspecialidadRepository


class TipoEspecialidadService:
    @staticmethod
    def crear_tipo_especialidad(tipo_especialidad: TipoEspecialidad):
        TipoEspecialidadRepository.crear(tipo_especialidad)

    @staticmethod
    def buscar_por_id(id: int) -> TipoEspecialidad:
        return TipoEspecialidadRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[TipoEspecialidad]:
        return TipoEspecialidadRepository.buscar_todos()

    @staticmethod
    def actualizar_tipo_especialidad(id: int, tipo_especialidad: TipoEspecialidad) -> TipoEspecialidad:
        tipo_especialidad_existente = TipoEspecialidadRepository.buscar_por_id(id)
        if not tipo_especialidad_existente:
            return None

        tipo_especialidad_existente.nombre = tipo_especialidad.nombre
        tipo_especialidad_existente.nivel = tipo_especialidad.nivel

        return TipoEspecialidadRepository.actualizar_tipo_especialidad(tipo_especialidad_existente)

    @staticmethod
    def borrar_por_id(id: int) -> TipoEspecialidad:
        return TipoEspecialidadRepository.borrar_por_id(id)

