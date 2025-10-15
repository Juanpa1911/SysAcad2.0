from marshmallow import Schema, fields, post_load, validate
from app.models import Facultad

class FacultadMapping(Schema):
    hashid = fields.String(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    abreviatura = fields.String(required=True, validate=validate.Length(min=1, max=10))
    directorio = fields.String(required=False, allow_none=True, validate=validate.Length(max=100))
    sigla = fields.String(required=False, allow_none=True, validate=validate.Length(max=10))
    codigoPostal = fields.String(required=False, allow_none=True, validate=validate.Length(max=10))
    ciudad = fields.String(required=False, allow_none=True, validate=validate.Length(max=50))
    domicilio = fields.String(required=False, allow_none=True, validate=validate.Length(max=100))
    telefono = fields.String(required=False, allow_none=True, validate=validate.Length(max=20))
    universidad_id = fields.Integer(required=True)
    
    @post_load
    def nueva_facultad(self, data, **kwargs):
        return Facultad(**data)