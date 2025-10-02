from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class TipoDedicacion(HashidMixin, db.Model):
    __tablename__ = 'tipos_dedicacion'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False) 
    observacion: str = db.Column(db.String(255), nullable=True)
    
    #relaciones