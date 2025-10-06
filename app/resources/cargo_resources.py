from flask import jsonify, Blueprint, request
from app.services import CargoService
from app.mapping.cargo_mapping import CargoMapping

cargo_bp = Blueprint('cargo', __name__)
cargo_mapping = CargoMapping()

@cargo_bp.route('/cargo', methods=['GET'])
def buscar_todos():
    cargo= CargoService.buscar_todos()
    return cargo_mapping.dump(cargo, many=True), 200

@cargo_bp.route('/cargo/<int:cargo_id>', methods=['GET'])
def buscar_cargo_id(cargo_id):
    cargo = CargoService.buscar_por_id(cargo_id)
    if cargo:
        return cargo_mapping.dump(cargo), 200
    return jsonify({"message": "Cargo not found"}), 404

@cargo_bp.route('/cargo', methods=['POST'])
def crear_cargo():
    cargo = cargo_mapping.load(request.get_json())
    CargoService.crear_cargo(cargo)
    return jsonify("Cargo creado exitosamente"), 200

@cargo_bp.route('/cargo/<int:cargo_id>', methods=['PUT'])
def actualizar_cargo(cargo_id):
    cargo = cargo_mapping.load(request.get_json())
    CargoService.actualizar_cargo(cargo_id, cargo)
    return jsonify("Cargo actualizado exitosamente"), 200

@cargo_bp.route('/cargo/<int:cargo_id>', methods=['DELETE'])
def borrar_cargo(cargo_id):
    CargoService.borrar_por_id(cargo_id)
    return jsonify("Cargo borrado exitosamente"), 200





