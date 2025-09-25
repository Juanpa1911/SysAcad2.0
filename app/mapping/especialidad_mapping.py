from marshmallow import Schema, fields, post_load, validate
from app.models import Especialidad

class EspelicalidadMapping(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    letra = fields.Str(required=True, validate=validate.Length(min=1, max=5))
    observacion = fields.Str(validate=validate.Length(max=200))

    @post_load
    def crear_especialidad(self, data, **kwargs):
        return Especialidad(**data)
