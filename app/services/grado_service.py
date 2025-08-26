from app.models.grado import Grado
from app.repositories.grado_repositorio import GradoRepository


class GradoService:
    @staticmethod
    def crear_grado(grado: Grado):
        GradoRepository.crear(grado)

    @staticmethod
    def buscar_por_id(id: int) -> Grado:
        return GradoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Grado]:
        return GradoRepository.buscar_todos()

    @staticmethod
    def actualizar_grado(id: int, grado: Grado) -> Grado:
        grado_existente = GradoRepository.buscar_por_id(id)
        if not grado_existente:
            return None
        grado_existente.nombre = grado.nombre
        return GradoRepository.actualizar_grado(grado_existente)

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return GradoRepository.borrar_por_id(id)
