from app import db
from app.models import TipoDocumento

class TipoDocumentoRepository:
    
    @staticmethod
    def crear_tipo_documento(tipo_documento):
        """Crea un nuevo tipo de documento en la base de datos"""
        db.session.add(tipo_documento)
        db.session.commit()
        return tipo_documento
    
    @staticmethod
    def buscar_todos():
        """Obtiene todos los tipos de documentos"""
        return TipoDocumento.query.all()
    
    @staticmethod
    def buscar_documento_id(tipo_documento_id):
        """Obtiene un tipo de documento por su ID"""
        return TipoDocumento.query.get(tipo_documento_id)
    
    @staticmethod
    def actualizar_tipo_documento(tipo_documento):
        """Actualiza un tipo de documento existente"""
        db.session.commit()
        return tipo_documento
    
    @staticmethod
    def borrar_tipo_documento_id(tipo_documento_id):
        """Elimina un tipo de documento por su ID"""
        tipo_documento = TipoDocumentoRepository.buscar_documento_id(tipo_documento_id)
        if tipo_documento:
            db.session.delete(tipo_documento)
            db.session.commit()
        return True
    
    @staticmethod
    def buscar_por_nombre(nombre):
        """Busca un tipo de documento por su nombre"""
        return TipoDocumento.query.filter_by(nombre=nombre).first()
    