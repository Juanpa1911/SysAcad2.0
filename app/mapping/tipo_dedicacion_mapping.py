from marshmallow import Schema, fields, post_load, validate
from app.models import TipoDedicacion

class TipoDedicacionMapping(Schema):
    hashid = fields.Str(dump_only=True)
    nombre = fields.Str(required=True)
    observacion = fields.String(required=False, allow_none=True, validate=validate.Length(max=255))
    #TODO no se si va observacion

    @post_load
    def crear_tipo_dedicacion(self, data, **kwargs):
        return TipoDedicacion(**data)
