from flask import jsonify, Blueprint, request
from app.services import GradoService
from app.mapping.grado_mapping import GradoMapping  

grado_bp = Blueprint('grado', __name__)
grado_mapping = GradoMapping()  


@grado_bp.route('/grado', methods=['GET'])
def buscar_todos():
    grados = GradoService.buscar_todos()
    return grado_mapping.dump(grados, many=True), 200   

@grado_bp.route('/grado/<hashid:id>', methods=['GET'])
def buscar_grado_id(id):
    grado = GradoService.buscar_por_id(id)
    if grado:
        return grado_mapping.dump(grado), 200
    return jsonify({"message": "Grado no encontrado"}), 404

@grado_bp.route('/grado', methods=['POST'])
def crear_grado():
    data = request.get_json()
    nuevo_grado = grado_mapping.load(data)
    GradoService.crear_grado(nuevo_grado)
    return grado_mapping.dump(nuevo_grado), 201

@grado_bp.route('/grado/<hashid:id>', methods=['PUT'])
def actualizar_grado(id):   
    data = request.get_json()
    datos_actualizados = grado_mapping.load(data)
    grado_actualizado = GradoService.actualizar_grado(
        id, datos_actualizados)
    if grado_actualizado:
        return grado_mapping.dump(grado_actualizado), 200
    return jsonify({"message": "Grado no encontrado"}), 404

@grado_bp.route('/grado/<hashid:id>', methods=['DELETE'])
def eliminar_grado(id):
    grado = GradoService.borrar_por_id(id)
    if grado:
        return jsonify({"message": "Grado eliminado"}), 200
    return jsonify({"message": "Grado no encontrado"}), 404