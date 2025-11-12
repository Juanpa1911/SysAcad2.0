from marshmallow.fields import String
from app import db
from datetime import date
from dataclasses import dataclass
from flask_hashids import HashidMixin

@dataclass(init=False, repr=True, eq=True)
class Alumno(HashidMixin, db.Model):
    __tablename__ = 'alumnos'
    
    id : int = db.Column(db.Integer, primary_key=True)
    apellido : str = db.Column(db.String(100), nullable=False)
    nombre : str = db.Column(db.String(100), nullable=False)
    nro_documento : str = db.Column(db.String(20), unique=True, nullable=False)
    tipo_documento_id : int = db.Column(db.Integer, db.ForeignKey('tipos_documento.id'), nullable=False)
    tipo_documento = db.relationship('TipoDocumento')
    fecha_nacimiento: String = db.Column(db.String(10), nullable=False)  # formato YYYY-MM-DD
    sexo : str = db.Column(db.String(1), nullable=False)  # 'M' o 'F'
    nro_legajo: int = db.Column(db.Integer, unique=True, nullable=False)
    fecha_ingreso: date = db.Column(db.Date, nullable=False, default=date.today)
    
    
               