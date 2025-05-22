from dataclasses import dataclass
from app.models.orientacion import Orientacion
from app import db

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = 'materias'
    idMateria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    observacion = db.Column(db.String(255), nullable=True)
    orientacion_id = db.Column(db.Integer, db.ForeignKey('orientaciones.id'))
    orientacion = db.relationship('Orientacion', backref='materias')
