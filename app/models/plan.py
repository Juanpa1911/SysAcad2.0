from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
    __tablename__ = 'planes'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    fecha_inicio: str = db.Column(db.String(10), nullable=True)
    fecha_fin: str = db.Column(db.String(10), nullable=True)
    observacion: str = db.Column(db.String(255), nullable=True)

    # Relación con Orientación (similar a Materia)
    orientacion_id: int = db.Column(
        db.Integer, db.ForeignKey('orientaciones.id'))
    orientacion = db.relationship('Orientacion')
