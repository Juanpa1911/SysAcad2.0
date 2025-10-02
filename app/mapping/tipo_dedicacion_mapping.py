from marshmallow import Schema, fields, post_load
from app.models import TipoDedicacion

class TipoDedicacionMapping(Schema):
    hashid = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    #TODO no se si va observacion

    @post_load
    def crear_tipo_dedicacion(self, data, **kwargs):
        return TipoDedicacion(**data)
