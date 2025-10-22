from flask import jsonify, Blueprint, request
from app.services import AutoridadService
from app.mapping.autoridad_mapping import AutoridadMapping

autoridad_bp = Blueprint('autoridad', __name__)
autoridad_mapping = AutoridadMapping()


@autoridad_bp.route('/autoridad', methods=['GET'])
def buscar_todos():
    autoridad = AutoridadService.obtener_todas_las_autoridades()
    return autoridad_mapping.dump(autoridad, many=True), 200


@autoridad_bp.route('/autoridad/<hashid:id>', methods=['GET'])
def buscar_autoridad_id(id):
    autoridad = AutoridadService.obtener_autoridad_por_id(id)
    if autoridad:
        return autoridad_mapping.dump(autoridad), 200
    return jsonify({"message": "Autoridad not found"}), 404


@autoridad_bp.route('/autoridad',  methods=['POST'])
def crear_autoridad():
    autoridad = autoridad_mapping.load(request.get_json())
    AutoridadService.crear_autoridad(autoridad)
    return jsonify("Autoridad creada exitosamente"), 200


@autoridad_bp.route('/autoridad/<hashid:id>', methods=['PUT'])
def actualizar_autoridad(id):
    autoridad = autoridad_mapping.load(request.get_json())
    AutoridadService.actualizar_autoridad(id, autoridad)
    return jsonify("Autoridad actualizada exitosamente"), 200


@autoridad_bp.route('/autoridad/<hashid:id>', methods=['DELETE'])
def borrar_autoridad(id):
    autoridad = AutoridadService.borrar_autoridad_por_id(id)
    if autoridad:
        return jsonify("Autoridad eliminada exitosamente"), 200
    return jsonify({"message": "Autoridad not found"}), 404
