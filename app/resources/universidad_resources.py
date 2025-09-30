from flask import jsonify, Blueprint, request
from app.services import UniversidadService
from app.mapping.universidad_mapping import UniversidadMapping

universidad_bp = Blueprint('universidad', __name__)
universidad_mapping = UniversidadMapping()

@universidad_bp.route('/universidad', methods=['GET'])
def index():
    universidades = UniversidadService.buscar_todos()
    return universidad_mapping.dump(universidades, many=True), 200

@universidad_bp.route('/universidad/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    universidad = UniversidadService.buscar_por_id(id)
    if not universidad:
        return {"message": "Universidad no encontrada"}, 404
    return universidad_mapping.dump(universidad), 200

@universidad_bp.route('/universidad', methods=['POST'])
def crear_universidad():
    universidad = universidad_mapping.load(request.get_json())
    UniversidadService.crear_universidad(universidad)
    return jsonify({"message": "Universidad creada exitosamente"}), 201


@universidad_bp.route('/universidad/<hashid:id>', methods=['PUT'])
def actualizar_universidad(id):
    universidad = universidad_mapping.load(request.get_json())
    UniversidadService.actualizar_universidad(id, universidad)
    return jsonify("Universidad actualizada exitosamente"), 200

