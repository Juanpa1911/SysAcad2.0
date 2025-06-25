from app.models import TipoDedicacion
from app.repositories import TipoDedicacionRepository

class TipoDedicacionService:
    """
    Clase de servicio para la entidad Tipo Dedicacion
    """
    @staticmethod
    def crear_tipo_dedicacion(tipo_dedicacion: TipoDedicacion):
        """
        Crea un nuevo tipo de dedicación en la base de datos.
        :param tipo_dedicacion: Objeto TipoDedicacion a crear.
        :return: Objeto TipoDedicacion creado.
        """
        TipoDedicacionRepository.crear(tipo_dedicacion)

    @staticmethod
    def buscar_por_id(id: int) -> TipoDedicacion:
        """
        Busca un tipo de dedicación por su ID.
        :param id: ID del tipo de dedicación a buscar.
        :return: Objeto TipoDedicacion encontrado o None si no se encuentra.
        """
        return TipoDedicacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[TipoDedicacion]:
        """
        Busca todos los tipos de dedicación en la base de datos.
        :return: Lista de objetos TipoDedicacion.
        """
        return TipoDedicacionRepository.buscar_todos()
    
    @staticmethod
    def actualizar_tipo_dedicacion(id: int, tipo_dedicacion: TipoDedicacion) -> TipoDedicacion:
        """
        Actualiza un tipo de dedicación existente en la base de datos.
        :param id: ID del tipo de dedicación a actualizar.
        :param tipo_dedicacion: Objeto TipoDedicacion con los nuevos datos.
        :return: Objeto TipoDedicacion actualizado o None si no se encuentra.
        """
        tipo_dedicacion_existente= TipoDedicacionRepository.buscar_por_id(id)
        if not tipo_dedicacion_existente:
            return None
        tipo_dedicacion_existente.nombre= tipo_dedicacion.nombre
        tipo_dedicacion_existente.observacion = tipo_dedicacion.observacion
        
        return tipo_dedicacion_existente
    
    @staticmethod
    def borrar_por_id(id:int) -> TipoDedicacion:
        """
        Borra un tipo de dedicación por su ID.
        :param id: ID del tipo de dedicación a borrar.
        :return: Objeto TipoDedicacion borrado o None si no se encuentra.
        """
        tipo_dedicacion = TipoDedicacionRepository.borrar_por_id(id)
        if not tipo_dedicacion:
            return None
        return tipo_dedicacion

