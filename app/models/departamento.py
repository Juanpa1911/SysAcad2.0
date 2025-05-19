from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Departamento(db.Model):
    __tablename__ = 'departamentos'
    # Se recomienda agregar un campo 'id' como clave primaria para mayor flexibilidad y buenas prácticas.
    # Si en el futuro se necesita relacionar la clase departameto con otras tablas, es mejor tener un campo 'id' como clave primaria.
    # Ejemplo:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False, unique=True)
    descripcion: str = db.Column(db.String(255), nullable=True)
    # Actualmente, 'nombre' es la clave primaria. Si los nombres pueden repetirse o cambiar, usar 'id' es mejor.
