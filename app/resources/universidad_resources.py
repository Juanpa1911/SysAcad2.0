from flask import jsonify, Blueprint, request
from app.services import UniversidadService
from app.mapping import UniversidadMapping
from markupsafe import escape

from app.validators import validate_with

universidad_bp = Blueprint('universidad', __name__)
universidad_mapping = UniversidadMapping()

@universidad_bp.route('/universidad', methods=['GET'])
def index():
    universidades = UniversidadService.buscar_todos()
    return universidad_mapping.dump(universidades, many=True), 200

@universidad_bp.route('/universidad/<int:id>', methods=['GET'])
def buscar_por_id(id:int):
    universidad = UniversidadService.buscar_por_id(id)
    return universidad_mapping.dump(universidad), 200

@universidad_bp.route('/universidad', methods=['POST'])
def crear_universidad():
    universidad_data = sanitize_universidad_input(request)
    universidad = UniversidadService.crear(universidad_data)
    return universidad_mapping.dump(universidad), 201


@universidad_bp.route('/universidad/<int:id>', methods=['PUT'])
@validate_with(UniversidadMapping)
def actualizar_universidad(id:int):
    universidad_data = universidad.mapping.load(request.json())
    universidad = UniversidadService.actualizar(id, universidad_data)
    return universidad_mapping.dump(universidad), 200


def sanitize_universidad_input(request):
    universidad_data = universidad_mapping.load(request.json())
    universidad_data.nombre = escape(universidad_data.nombre)
    universidad_data.sigla = escape(universidad_data.sigla)
    return universidad_data