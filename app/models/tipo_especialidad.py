from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class TipoEspecialidad(db.Model):
    _tablename_ = 'tipos especialidades'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    nivel : str = db.Column(db.String(10), nullable= False)