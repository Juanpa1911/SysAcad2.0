from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Grupo(db.Model):
    __tablename__ = 'grupos'
    # Se recomienda agregar un campo 'id' como clave primaria para mayor flexibilidad y buenas prácticas.
    # Si en el futuro se necesita relacionar la clase grupo con otras tablas, es mejor tener un campo 'id' como clave primaria.
    # Ejemplo:
    # id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # nombre: str = db.Column(db.String(100), nullable=False, unique=True)
    # Actualmente, 'nombre' es la clave primaria. Si los nombres pueden repetirse o cambiar, usar 'id' es mejor.
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre : str = db.Column(db.String(100), nullable=False, unique=True)