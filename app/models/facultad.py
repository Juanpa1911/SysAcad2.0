from dataclasses import dataclass
from app import db
from sqlalchemy import ForeignKey


@dataclass(init=False, repr=True, eq=True)
class Facultad(db.Model):
    __tablename__ = 'facultades'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    abreviatura: str = db.Column(db.String(10), nullable=False)  # NOT NULL
    directorio: str = db.Column(db.String(100), nullable=True)
    sigla: str = db.Column(db.String(10), nullable=True)
    codigo_postal: str = db.Column(db.String(10), nullable=True)
    ciudad: str = db.Column(db.String(50), nullable=True)
    domicilio: str = db.Column(db.String(100), nullable=True)
    telefono: str = db.Column(db.String(20), nullable=True)
    contacto: str = db.Column(db.String(100), nullable=True)
    email: str = db.Column(db.String(100), nullable=True)
    universidad_id: int = db.Column(
        db.Integer, ForeignKey('universidades.id'), nullable=False)

    universidad = db.relationship('Universidad', back_populates='facultades')
