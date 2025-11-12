from flask import jsonify, Blueprint, request
from app.services import OrientacionService
from app.mapping.orientacion_mapping import OrientacionMapping

orientacion_bp = Blueprint('orientacion', __name__)
orientacion_mapping = OrientacionMapping()

@orientacion_bp.route('/orientacion', methods=['GET'])
def buscar_todos():
    orientaciones = OrientacionService.buscar_todos()
    return orientacion_mapping.dump(orientaciones, many=True), 200

@orientacion_bp.route('/orientacion/<hashid:id>', methods=['GET'])
def buscar_orientacion_id(id):
    orientacion = OrientacionService.buscar_por_id(id)
    if orientacion:
        return orientacion_mapping.dump(orientacion), 200
    return jsonify({"message": "Orientación no encontrada"}), 404

@orientacion_bp.route('/orientacion', methods=['POST'])
def crear_orientacion():
    data = request.get_json()
    orientacion = orientacion_mapping.load(data)
    OrientacionService.crear_orientacion(orientacion)
    return orientacion_mapping.dump(orientacion), 201

@orientacion_bp.route('/orientacion/<hashid:id>', methods=['PUT'])
def actualizar_orientacion(id):
    data = request.get_json()
    datos_actualizados = orientacion_mapping.load(data)
    orientacion_actualizada = OrientacionService.actualizar_orientacion(
        id, datos_actualizados)
    if orientacion_actualizada:
        return orientacion_mapping.dump(orientacion_actualizada), 200
    return jsonify({"message": "Orientación no encontrada"}), 404

@orientacion_bp.route('/orientacion/<hashid:id>', methods=['DELETE'])
def eliminar_orientacion(id):
    orientacion = OrientacionService.borrar_por_id(id)
    if orientacion:
        return jsonify({"message": "Orientación eliminada"}), 200
    return jsonify({"message": "Orientación no encontrada"}), 404

