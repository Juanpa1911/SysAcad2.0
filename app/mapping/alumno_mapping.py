from marshmallow import Schema, fields
from app.models import Alumno

class AlumnoMapping(Schema):
    id = fields.Integer(dump_only=True)
    nro_legajo = fields.String(required=True)
    apellido = fields.String(required=True)
    nombre = fields.String(required=True)
    nro_documento = fields.String(required=True)
    tipo_documento_id = fields.Integer(required=True)
    fecha_nacimiento = fields.String(required = True)
    sexo = fields.String(required = True)
    fecha_ingreso = fields.Date(required = True)
    facultad_id = fields.Integer(required=True)
    
    facultad = fields.Nested('FacultadMapping', dump_only=True)

class AlumnoFichaMapping(Schema):
    nro_legajo = fields.String()
    apellido = fields.String()
    nombre = fields.String()
    nro_documento = fields.String()
    tipo_documento_id = fields.String()
    fecha_nacimiento  = fields.String()
    sexo  = fields.String()
    fecha_ingreso  = fields.Date()
    facultad_nombre = fields.Method("get_facultad_nombre")
    facultad_abreviatura = fields.Method("get_facultad_abreviatura")
    
    def get_facultad_nombre(self, obj):
        return obj.facultad.nombre if obj.facultad else None
    
    def get_facultad_abreviatura(self, obj):
        return obj.facultad.abreviatura if obj.facultad else None