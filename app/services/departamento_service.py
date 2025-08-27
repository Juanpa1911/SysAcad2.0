from app.models import Departamento
from app.repositories.departamento_repositorio import DepartamentoRepository

class DepartamentoService:
    '''
    Clase de servicio para la entidad Departamento.
    '''
    @staticmethod
    def crear_departamento(departamento: Departamento):
        DepartamentoRepository.crear(departamento)
    
    @staticmethod
    def buscar_por_id(id: int) -> Departamento:
        return DepartamentoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Departamento]:
        return DepartamentoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_departamento(id: int, departamento: Departamento) -> Departamento:
        departamento_existente = DepartamentoRepository.buscar_por_id(id)
        if not departamento_existente:
            return None
        departamento_existente.nombre = departamento.nombre
        departamento_existente.descripcion = departamento.descripcion
        return DepartamentoRepository.actualizar_departamento(departamento_existente)
    
    @staticmethod
    def borrar_por_id(id: int) -> Departamento:
        departamento = DepartamentoRepository.borrar_por_id(id)
        if not departamento:
            return None
        return departamento