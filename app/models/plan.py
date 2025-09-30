from dataclasses import dataclass
from app import db
from datetime import date

@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
    __tablename__ = 'planes'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)

   #Uso de DateTime en lugar de String
    fecha_inicio: date = db.Column(db.Date, nullable=False, default=date.today)
    fecha_fin: date = db.Column(db.Date, nullable=True)

    observacion: str = db.Column(db.String(255), nullable=True)
    orientacion_id: int = db.Column(db.Integer, db.ForeignKey('orientaciones.id'), nullable=True)
    orientacion = db.relationship('Orientacion')

    def validar_fechas(self):
        if self.fecha_fin and self.fecha_inicio >= self.fecha_fin:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha de fin.") 