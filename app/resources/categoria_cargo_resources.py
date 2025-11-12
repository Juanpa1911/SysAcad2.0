from flask import jsonify, Blueprint, request
from app.services import CategoriaCargoService
from app.mapping.categoria_cargo_mapping import CategoriaCargoMapping

categoria_cargo_bp = Blueprint('categoria_cargo', __name__)
categoria_cargo_mapping = CategoriaCargoMapping()
@categoria_cargo_bp.route('/categoria_cargo', methods=['GET'])
def buscar_todos():
    categoria_cargo= CategoriaCargoService.buscar_todos()
    return categoria_cargo_mapping.dump(categoria_cargo, many=True), 200

@categoria_cargo_bp.route('/categoria_cargo/<hashid:categoria_cargo_id>', methods=['GET'])
def buscar_categoria_cargo_id(categoria_cargo_id):
    categoria_cargo = CategoriaCargoService.buscar_por_id(categoria_cargo_id)
    if categoria_cargo:
        return categoria_cargo_mapping.dump(categoria_cargo), 200
    return jsonify({"message": "CategoriaCargo not found"}), 404

@categoria_cargo_bp.route('/categoria_cargo', methods=['POST'])
def crear_categoria_cargo():
    categoria_cargo = categoria_cargo_mapping.load(request.get_json())
    CategoriaCargoService.crear_categoria_cargo(categoria_cargo)
    return jsonify("CategoriaCargo creado exitosamente"), 200

@categoria_cargo_bp.route('/categoria_cargo/<hashid:categoria_cargo_id>', methods=['PUT'])
def actualizar_categoria_cargo(categoria_cargo_id):
    categoria_cargo = categoria_cargo_mapping.load(request.get_json())
    CategoriaCargoService.actualizar_categoria_cargo(categoria_cargo_id, categoria_cargo)
    return jsonify("CategoriaCargo actualizado exitosamente"), 200
@categoria_cargo_bp.route('/categoria_cargo/<hashid:categoria_cargo_id>', methods=['DELETE'])

def borrar_categoria_cargo(categoria_cargo_id):
    CategoriaCargoService.borrar_por_id(categoria_cargo_id)
    return jsonify("CategoriaCargo borrado exitosamente"), 200

