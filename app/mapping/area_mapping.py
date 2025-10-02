from marshmallow import Schema, fields, post_load, validate
from app.models import Area

class AreaMapping(Schema):
    hashid = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    
    @post_load
    def nueva_area(self, data, **kwargs):
        return Area(**data)