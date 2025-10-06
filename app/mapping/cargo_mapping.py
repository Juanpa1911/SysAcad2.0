from marshmallow import Schema, fields, post_load, validate
from app.models import Cargo

class CargoMapping(Schema):
    hashid = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    puntos = fields.Int(required=True, validate=validate.Range(min=0))
    
    categoria_cargo_id = fields.Int(required=True)
    tipo_dedicacion_id = fields.Int(required=True)

    @post_load
    def crear_cargo(self, data, **kwargs):
        return Cargo(**data)