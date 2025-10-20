from marshmallow import Schema, fields, post_load, validate
from app.models import CategoriaCargo


class CategoriaCargoSchema(Schema):
    id = fields.Int(required=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    descripcion = fields.Str(required=True, validate=validate.Length(min=2, max=200))

    @post_load
    def create_categoria_cargo(self, data, **kwargs):
        return CategoriaCargo(**data)
