from marshmallow import Schema, fields, post_load
from app.models import Orientacion

class OrientacionMapping(Schema):
    hashid = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    #TODO no se si va materias, en ese caso, no se como va

    @post_load
    def crear_orientacion(self, data, **kwargs):
        return Orientacion(**data)
