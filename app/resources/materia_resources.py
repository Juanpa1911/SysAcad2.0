from flask import jsonify, Blueprint, request
from app.services import MateriaService
from app.mapping.materia_mapping import MateriaMapping

materia_bp = Blueprint('materia', __name__)
materia_mapping = MateriaMapping()

@materia_bp.route('/materia', methods=['GET'])
def buscar_todos():
    materias = MateriaService.buscar_todos()
    return materia_mapping.dump(materias, many=True), 200

@materia_bp.route('/materia/<hashid:id>', methods=['GET'])
def buscar_materia_id(id):
    materia = MateriaService.buscar_por_id(id)
    if materia:
        return materia_mapping.dump(materia), 200
    return jsonify({"message": "Materia no encontrada"}), 404

@materia_bp.route('/materia', methods=['POST'])
def crear_materia():
    data = request.get_json()
    materia = materia_mapping.load(data)
    MateriaService.crear_materia(materia)
    return materia_mapping.dump(materia), 201

@materia_bp.route('/materia/<hashid:id>', methods=['PUT'])
def actualizar_materia(id):
    data = request.get_json()
    datos_actualizados = materia_mapping.load(data)
    materia_actualizada = MateriaService.actualizar_materia(
        id, datos_actualizados)
    if materia_actualizada:
        return materia_mapping.dump(materia_actualizada), 200
    return jsonify({"message": "Materia no encontrada"}), 404

@materia_bp.route('/materia/<hashid:id>', methods=['DELETE'])
def eliminar_materia(id):
    materia = MateriaService.borrar_por_id(id)
    if materia:
        return jsonify({"message": "Materia eliminada"}), 200
    return jsonify({"message": "Materia no encontrada"}), 404
    
