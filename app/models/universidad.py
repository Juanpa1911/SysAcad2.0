from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Universidad(db.Model):
    __tablename__ = 'universidades'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    sigla : str = db.Column(db.String(10), nullable=False) 
    #TODO hacer la relacion con facultades, 1 a muchas
    
    facultades = db.relationship(
        'Facultad',
        back_populates='universidad',
        lazy='dynamic',
        cascade="all, delete-orphan"  # TODO Elimina facultades asociadas automáticamente
    )    
    def asociar_facultad(self, facultad):
        if facultad not in self.facultades:
            facultad.universidad = self  # Asocia la facultad a esta universidad
            db.session.add(facultad)