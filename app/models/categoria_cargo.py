from dataclasses import dataclass
from app import db
from flask_hashids import HashidMixin


@dataclass(init=False, repr=True, eq=True)
class CategoriaCargo(HashidMixin, db.Model):
    __tablename__ = 'categorias_cargos'
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre : str = db.Column(db.String(100), nullable=False)
    
    # Relaciones
    #cargos = db.relationship('Cargo', backref='categoria_cargo', lazy=True)
