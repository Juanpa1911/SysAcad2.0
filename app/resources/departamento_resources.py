from flask import jsonify, Blueprint, request
from app.services import DepartamentoService
from app.mapping.departamento_mapping import DepartamentoMapping

departamento_bp = Blueprint('departamento', __name__)
departamento_mapping = DepartamentoMapping()

@departamento_bp.route('/departamento', methods=['GET'])
def buscar_todos():
    departamentos = DepartamentoService.buscar_todos()
    return departamento_mapping.dump(departamentos, many=True), 200

@departamento_bp.route('/departamento/<hashid:id>', methods=['GET'])
def buscar_departamento_id(id):
    departamento = DepartamentoService.buscar_por_id(id)
    if departamento:
        return departamento_mapping.dump(departamento), 200
    return jsonify({"message": "Departamento no encontrado"}), 404

@departamento_bp.route('/departamento', methods=['POST'])
def crear_departamento():
    data = request.get_json()
    departamento = departamento_mapping.load(data)
    DepartamentoService.crear_departamento(departamento)
    return departamento_mapping.dump(departamento), 201

@departamento_bp.route('/departamento/<hashid:id>', methods=['PUT'])
def actualizar_departamento(id):
    data = request.get_json()
    datos_actualizados = departamento_mapping.load(data)
    departamento_actualizado = DepartamentoService.actualizar_departamento(datos_actualizados, id)
    if departamento_actualizado:
        return departamento_mapping.dump(departamento_actualizado), 200
    return jsonify({"message": "Departamento no encontrado"}), 404

@departamento_bp.route('/departamento/<hashid:id>', methods=['DELETE'])
def eliminar_departamento(id):
    departamento = DepartamentoService.borrar_por_id(id)
    if departamento:
        return jsonify({"message": "Departamento eliminado"}), 200
    return jsonify({"message": "Departamento no encontrado"}), 404