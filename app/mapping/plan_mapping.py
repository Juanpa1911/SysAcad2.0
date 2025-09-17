from marshmallow import Schema, fields, post_load, validate
from app.models import Plan

class PlanMapping(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    fecha_inicio = fields.DateTime(required=True)
    fecha_fin = fields.DateTime(allow_none=True)
    observacion = fields.Str(allow_none=True, validate=validate.Length(max=255))
    orientacion_id = fields.Int(required=True)

    @post_load
    def crear_plan(self, data, **kwargs):
        return Plan(**data)
