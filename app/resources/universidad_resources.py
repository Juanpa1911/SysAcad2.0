from flask import jsonify, Blueprint
from app.services import universidad_service
from app.mapping.universidad_mapping import UniversidadMapping

universidad_bp = Blueprint('universidad', __name__)
universidad_mapping = UniversidadMapping()

@universidad_bp.route('/universidad', methods=['GET'])
def index():
    universidades = universidad_service.buscar_todos()
    return universidad_mapping.dump(universidades, many=True), 200

@universidad_bp.route('/universidad', methods=['GET'])
def buscar_por_id(id):
    universidad = universidad_service.buscar_por_id(id)
    return universidad_mapping.dump(universidad), 200