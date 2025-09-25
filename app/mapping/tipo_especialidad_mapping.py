from marshmallow import Schema, fields, post_load, validate
from app.models import TipoEspecialidad

class TipoEspecialidadMapping(Schema):
    id=fields.Int(dump_only=True)
    nombre=fields.Str(required=True, validate=validate.Length(min=1, max=100))
    nivel=fields.Str(required=True, validate=validate.Length(min=1, max=10))

    @post_load
    def crear_tipo_especialidad(self, data, **kwargs):
        return TipoEspecialidad(**data)
    



    