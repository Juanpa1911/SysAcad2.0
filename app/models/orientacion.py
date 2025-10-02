from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Orientacion(HashidMixin, db.Model):
    __tablename__ = 'orientaciones'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    
    materias = db.relationship('Materia', back_populates='orientacion' )
    
#relacion con materias
