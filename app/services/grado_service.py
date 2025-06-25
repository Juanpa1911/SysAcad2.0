from app.models.grado import Grado
from app.repositories.grado_repositorio import GradoRepository


class GradoService:
    
    """Clase de servicio para la entidad Grado."""

    @staticmethod
    def crear_grado(grado: Grado):
        """ 
        Crea un nuevo grado en la base de datos.
        :param grado: Objeto Grado a crear.
        :return: Objeto Grado creado.
        """
        GradoRepository.crear(grado)

    @staticmethod
    def buscar_por_id(id: int) -> Grado:
        """
        Busca un grado por su ID.
        :param id: ID del grado a buscar.
        :return: Objeto Grado encontrado o None si no se encuentra.
        """
        return GradoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Grado]:
        """
        Busca todos los grados en la base de datos.
        :return: Lista de objetos Grado.
        """
        return GradoRepository.buscar_todos()

    @staticmethod
    def actualizar_grado(id: int, grado: Grado) -> Grado:
        """
        Actualiza un grado existente en la base de datos.
        :param id: ID del grado a actualizar.
        :param grado: Objeto Grado con los nuevos datos.
        :return: Objeto Grado actualizado.
        """
        grado_existente = GradoRepository.buscar_por_id(id)
        if not grado_existente:
            return None
        grado_existente.nombre = grado.nombre
        return GradoRepository.actualizar_grado(grado_existente)

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        """
        Borra un grado por su ID.
        :param id: ID del grado a borrar.
        :return: True si se borra correctamente, False si no se encuentra.
        """
        return GradoRepository.borrar_por_id(id)
