from dataclasses import dataclass
from app import db



@dataclass(init=False, repr=True, eq=True)
class Cargo(db.Model):  
    __tablename__ = 'cargos'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False, unique=True)
    puntos: int = db.Column(db.Integer, nullable=False)

    # Claves foráneas
    categoria_cargo_id = db.Column(db.Integer, db.ForeignKey('categorias_cargos.id'))
    tipo_dedicacion_id = db.Column(db.Integer, db.ForeignKey('tipos_dedicacion.id'))

    # Relaciones
    categoria_cargo = db.relationship('CategoriaCargo')
    tipo_dedicacion = db.relationship('TipoDedicacion')

