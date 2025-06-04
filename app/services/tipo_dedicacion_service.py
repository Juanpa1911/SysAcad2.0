from app.models import TipoDedicacion
from app.repositories import TipoDedicacionRepository

class TipoDedicacionService:
    """
    Clase de servicio para la entidad Tipo Dedicacion
    """
    @staticmethod
    def crear_tipo_dedicacion(tipo_dedicacion: TipoDedicacion):
        TipoDedicacionRepository.crear(tipo_dedicacion)

    @staticmethod
    def buscar_por_id(id: int) -> TipoDedicacion:
        return TipoDedicacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[TipoDedicacion]:
        return TipoDedicacionRepository.buscar_todos()
    
    @staticmethod
    def actualizar_tipo_dedicacion(id: int, tipo_dedicacion: TipoDedicacion) -> TipoDedicacion:
        tipo_dedicacion_existente= TipoDedicacionRepository.buscar_por_id(id)
        if not tipo_dedicacion_existente:
            return None
        tipo_dedicacion_existente.nombre= tipo_dedicacion.nombre
        tipo_dedicacion_existente.observacion = tipo_dedicacion.observacion
        
        return tipo_dedicacion_existente
    
    @staticmethod
    def borrar_por_id(id:int) -> TipoDedicacion:
        tipo_dedicacion = TipoDedicacionRepository.borrar_por_id(id)
        if not tipo_dedicacion:
            return None
        return tipo_dedicacion

