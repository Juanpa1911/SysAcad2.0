from flask import jsonify, Blueprint, request
from app.services import FacultadService
from app.mapping.facultad_mapping import FacultadMapping

facultad_bp = Blueprint('facultad', __name__)
facultad_mapping = FacultadMapping()


@facultad_bp.route('/facultad', methods=['GET'])
def buscar_todos():
    facultades = FacultadService.buscar_todos()
    return facultad_mapping.dump(facultades, many=True), 200


@facultad_bp.route('/facultad/<hashid:id>', methods=['GET'])
def buscar_facultad_id(id):
    facultad = FacultadService.buscar_por_id(id)
    if facultad:
        return facultad_mapping.dump(facultad), 200
    return jsonify({"message": "Facultad no encontrada"}), 404


@facultad_bp.route('/facultad', methods=['POST'])
def crear_facultad():
    data = request.get_json()
    facultad = facultad_mapping.load(data)
    FacultadService.crear_facultad(facultad)
    return facultad_mapping.dump(facultad), 201


@facultad_bp.route('/facultad/<hashid:id>', methods=['PUT'])
def actualizar_facultad(id):
    data = request.get_json()
    datos_actualizados = facultad_mapping.load(data)
    facultad_actualizada = FacultadService.actualizar_facultad(
        id, datos_actualizados)
    if facultad_actualizada:
        return facultad_mapping.dump(facultad_actualizada), 200
    return jsonify({"message": "Facultad no encontrada"}), 404


@facultad_bp.route('/facultad/<hashid:id>', methods=['DELETE'])
def eliminar_facultad(id):
    facultad = FacultadService.borrar_por_id(id)
    if facultad:
        return jsonify({"message": "Facultad eliminada"}), 200
    return jsonify({"message": "Facultad no encontrada"}), 404
