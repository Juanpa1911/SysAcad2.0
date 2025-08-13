from marshmallow import Schema, fields, post_load 
from app.models import Universidad
from markupsafe import escape

class UniversidadMapping(Schema):
    id = fields.Integer(dump_only=True)
    #TODO agregar validaciones (largo de texto según modelo)
    nombre = fields.String(required = True)
    sigla = fields.String(required = True)

    @post_load
    def nueva_universidad(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = escape(value)
        return Universidad(**data) 