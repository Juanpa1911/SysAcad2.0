from app.repositories.tipo_doc_repositorio import TipoDocumentoRepository

class TipoDocumentoService:
    
    @staticmethod
    def crear_tipo_documento(tipo_documento):
        """Crea un nuevo tipo de documento en la base de datos"""
        return TipoDocumentoRepository.crear_tipo_documento(tipo_documento)

    @staticmethod
    def buscar_todos_doc():
        """Obtiene todos los tipos de documentos"""
        return TipoDocumentoRepository.buscar_todos()

    @staticmethod
    def buscar_documento_id(tipo_documento_id):
        """Obtiene un tipo de documento por su ID"""
        return TipoDocumentoRepository.buscar_documento_id(tipo_documento_id)

    @staticmethod
    def actualizar_tipo_documento(tipo_documento):
        """Actualiza un tipo de documento existente"""
        return TipoDocumentoRepository.actualizar_tipo_documento(tipo_documento)

    @staticmethod
    def borrar_tipo_documento_id(tipo_documento_id):
        """Elimina un tipo de documento por su ID"""
        return TipoDocumentoRepository.borrar_tipo_documento_id(tipo_documento_id)

    @staticmethod
    def buscar_por_nombre(nombre):
        """Busca un tipo de documento por su nombre"""
        return TipoDocumentoRepository.buscar_por_nombre(nombre)