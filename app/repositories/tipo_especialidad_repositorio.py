from app import db
from app.models.tipo_especialidad import TipoEspecialidad

class TipoEspecialidadRepository:
    @staticmethod
    def crear(tipo_especialidad: TipoEspecialidad):
        db.session.add(tipo_especialidad)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int) -> TipoEspecialidad:
        return db.session.query(TipoEspecialidad).filter_by(id=id).first()

    @staticmethod
    def buscar_todos() -> list[TipoEspecialidad]:
        return db.session.query(TipoEspecialidad).all()

    @staticmethod
    def actualizar_tipo_especialidad(tipo_especialidad: TipoEspecialidad) -> TipoEspecialidad:
        tipo_especialidad_existente = db.session.merge(tipo_especialidad)
        if not tipo_especialidad_existente:
            return None
        db.session.commit()
        return tipo_especialidad_existente

    @staticmethod
    def borrar_por_id(id: int) -> TipoEspecialidad:
        tipo_especialidad = db.session.query(TipoEspecialidad).filter_by(id=id).first()
        if not tipo_especialidad:
            return None
        db.session.delete(tipo_especialidad)
        db.session.commit()
        return tipo_especialidad