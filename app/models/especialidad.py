from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq= True)
class Especialidad(db.Model):
    __tablename__= 'especialidades'
    id: int = db.Column(db.Integer, primary_key= True, autoincrement= True)
    nombre: str = db.Column(db.String(100), nullable=True)
    letra: str = db.Column(db.String(10), nullable=True)
    observacion: str = db.Column(db.String(200), nullable=True)

    #Relaciones: