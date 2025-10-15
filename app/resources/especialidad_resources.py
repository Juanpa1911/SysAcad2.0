from flask import jsonify, Blueprint, request
from app.services import EspecialidadService
from app.mapping.especialidad_mapping import EspecialidadMapping

especialidad_bp = Blueprint('especialidad', __name__)
especialidad_mapping = EspecialidadMapping()


@especialidad_bp.route('/especialidad', methods=['GET'])
def buscar_todos():
    especialidades = EspecialidadService.buscar_todos()
    return especialidad_mapping.dump(especialidades, many=True), 200


@especialidad_bp.route('/especialidad/<hashid:id>', methods=['GET'])
def buscar_especialidad_id(id):
    especialidad = EspecialidadService.buscar_por_id(id)
    if especialidad:
        return especialidad_mapping.dump(especialidad), 200
    return jsonify({"message": "Especialidad no encontrada"}), 404


@especialidad_bp.route('/especialidad', methods=['POST'])
def crear_especialidad():
    data = request.get_json()
    nueva_especialidad = especialidad_mapping.load(data)
    EspecialidadService.crear_especialidad(nueva_especialidad)
    return especialidad_mapping.dump(nueva_especialidad), 201


@especialidad_bp.route('/especialidad/<hashid:id>', methods=['PUT'])
def actualizar_especialidad(id):
    data = request.get_json()
    datos_actualizados = especialidad_mapping.load(data)
    especialidad_actualizada = EspecialidadService.actualizar_especialidad(
        id, datos_actualizados)
    if especialidad_actualizada:
        return especialidad_mapping.dump(especialidad_actualizada), 200
    return jsonify({"message": "Especialidad no encontrada"}), 404


@especialidad_bp.route('/especialidad/<hashid:id>', methods=['DELETE'])
def eliminar_especialidad(id):
    especialidad = EspecialidadService.borrar_por_id(id)
    if especialidad:
        return jsonify({"message": "Especialidad eliminada"}), 200
    return jsonify({"message": "Especialidad no encontrada"}), 404
