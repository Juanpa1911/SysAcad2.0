from marshmallow import Schema, fields, post_load, validate
from app.models import Grado

class GradoMapping(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=50))

    @post_load
    def crear_grado(self, data, **kwargs):
        return Grado(**data)
