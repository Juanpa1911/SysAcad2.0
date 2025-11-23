from marshmallow import Schema, fields, post_load, validate
from app.models import TipoDocumento

class TipoDocumentoMapping(Schema):
    hashid = fields.Str(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))

    @post_load
    def crear_tipo_documento(self, data, **kwargs):
        return TipoDocumento(**data)
    

