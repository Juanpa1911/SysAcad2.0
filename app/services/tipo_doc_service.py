from app.repositories.tipo_doc_repositorio import TipoDocumentoRepository

class TipoDocumentoService:
    
    @staticmethod
    def crear_tipo_documento(tipo_documento):
        """
        Crea un nuevo tipo de documento en la base de datos
        :param tipo_documento: Objeto que representa el tipo de documento a crear
        :return: Objeto tipo documento creado
        """
        return TipoDocumentoRepository.crear_tipo_documento(tipo_documento)

    @staticmethod
    def buscar_todos_doc():
        """
        Obtiene todos los tipos de documentos
        :return: Lista de objetos tipo documento
        """
        return TipoDocumentoRepository.buscar_todos()

    @staticmethod
    def buscar_documento_id(tipo_documento_id):
        """
        Obtiene un tipo de documento por su ID
        :param tipo_documento_id: ID del tipo de documento a buscar
        :return: Objeto tipo documento encontrado o None si no existe
        """
        return TipoDocumentoRepository.buscar_documento_id(tipo_documento_id)

    @staticmethod
    def actualizar_tipo_documento(tipo_documento):
        """
        Actualiza un tipo de documento existente
        :param tipo_documento: Objeto que contiene los datos actualizados del tipo de documento
        :return: Objeto tipo documento actualizado
        """
        return TipoDocumentoRepository.actualizar_tipo_documento(tipo_documento)

    @staticmethod
    def borrar_tipo_documento_id(tipo_documento_id):
        """
        Elimina un tipo de documento por su ID
        :param tipo_documento_id: ID del tipo de documento a eliminar
        :return: Objeto tipo documento eliminado o None si no existe
        """
        return TipoDocumentoRepository.borrar_tipo_documento_id(tipo_documento_id)

    @staticmethod
    def buscar_por_nombre(nombre):
        """
        Busca un tipo de documento por su nombre
        :param nombre: Nombre del tipo de documento a buscar
        :return: Objeto tipo documento encontrado o None si no existe
        """
        return TipoDocumentoRepository.buscar_por_nombre(nombre)