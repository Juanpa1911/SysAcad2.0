from marshmallow import Schema, fields, post_load, validate
from app.models import Autoridad

class AutoridadMapping(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    telefono = fields.Str(validate=validate.Length(max=20))
    email = fields.Email(validate=validate.Length(max=100))

    @post_load
    def crear_autoridad(self, data, **kwargs):
        return Autoridad(**data)
    
    

