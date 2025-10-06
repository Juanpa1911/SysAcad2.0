from marshmallow import Schema, fields, post_load, validate
from app.models import Materia

class MateriaMapping(Schema):
    hashid = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    codigo = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    observacion = fields.Str(validate=validate.Length(max=255))
    orientacion_id = fields.Int(required=True)

    @post_load
    def crear_materia(self, data, **kwargs):
        return Materia(**data)