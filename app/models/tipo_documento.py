from app import db
from dataclasses import dataclass
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class TipoDocumento(HashidMixin, db.Model):
    __tablename__ = 'tipos_documento'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(50), nullable=False, unique=True)
    