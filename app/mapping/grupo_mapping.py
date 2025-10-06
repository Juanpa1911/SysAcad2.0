from marshmallow import Schema, fields, post_load, validate
from app.models import Grupo

class GrupoMapping(Schema):
    hashid = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def crear_grupo(self, data, **kwargs):
        return Grupo(**data)