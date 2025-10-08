from flask import jsonify, Blueprint, request
from app.services.tipo_dedicacion_service import TipoDedicacionService
from app.mapping.tipo_dedicacion_mapping import TipoDedicacionMapping

tipo_dedicacion_bp = Blueprint('tipo_dedicacion', __name__)
tipo_dedicacion_mapping = TipoDedicacionMapping()

@tipo_dedicacion_bp.route('/tipo_dedicacion', methods=['GET'])
def buscar_todos():
    tipos_dedicacion = TipoDedicacionService.buscar_todos()
    return tipo_dedicacion_mapping.dump(tipos_dedicacion, many=True), 200

@tipo_dedicacion_bp.route('/tipo_dedicacion/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    tipo_dedicacion = TipoDedicacionService.buscar_por_id(id)
    if not tipo_dedicacion:
        return {"message": "Tipo de dedicación no encontrado"}, 404
    return tipo_dedicacion_mapping.dump(tipo_dedicacion), 200

@tipo_dedicacion_bp.route('/tipo_dedicacion', methods=['POST'])
def crear_tipo_dedicacion():
    tipo_dedicacion = tipo_dedicacion_mapping.load(request.get_json())
    TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicacion)
    return jsonify("Tipo de dedicación creado exitosamente"), 200

@tipo_dedicacion_bp.route('/tipo_dedicacion/<hashid:id>', methods=['PUT'])
def actualizar_tipo_dedicacion(id):
    tipo_dedicacion = tipo_dedicacion_mapping.load(request.get_json())
    TipoDedicacionService.actualizar_tipo_dedicacion(id, tipo_dedicacion)
    return jsonify("Tipo de dedicación actualizado exitosamente"), 200

@tipo_dedicacion_bp.route('/tipo_dedicacion/<hashid:id>', methods=['DELETE'])
def borrar_tipo_dedicacion(id):
    TipoDedicacionService.borrar_por_id(id)
    return jsonify("Tipo de dedicación borrado exitosamente"), 200

