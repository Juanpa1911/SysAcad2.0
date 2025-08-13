from marshmallow import Schema, fields, post_load 
from app.models import Universidad
from markupsafe import escape

class UniversidadMapping(Schema):
    hashid = fields.String(dump_only=True)
    #TODO agregar validaciones (largo de texto según modelo)
    nombre = fields.String(required = True, validate = validate.Length(min=1, max=100))
    sigla = fields.String(required = True, validate = validate.Length(min=1, max=10))

    @post_load
    def nueva_universidad(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Universidad(**data) 