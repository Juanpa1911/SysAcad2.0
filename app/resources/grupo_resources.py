from flask import jsonify, Blueprint, request
from app.services import GrupoService
from app.mapping.grupo_mapping import GrupoMapping

grupo_bp = Blueprint('grupo', __name__)
grupo_mapping = GrupoMapping()

@grupo_bp.route('/grupo', methods=['GET'])
def buscar_todos():
    grupos = GrupoService.buscar_todos()
    return grupo_mapping.dump(grupos, many=True), 200


@grupo_bp.route('/grupo/<hashid:id>', methods=['GET'])
def buscar_grupo_id (id):
    grupo = GrupoService.buscar_por_id(id)
    if grupo:
        return grupo_mapping.dump(grupo), 200
    return jsonify({"message": "Grupo no encontrado"}), 404


@grupo_bp.route('/grupo', methods=['POST'])
def crear_grupo():
    data = request.get_json()
    nuevo_grupo = grupo_mapping.load(data)
    GrupoService.crear_grupo(nuevo_grupo)
    return grupo_mapping.dump(nuevo_grupo), 201


@grupo_bp.route('/grupo/<hashid:id>', methods=['PUT'])
def actualizar_grupo(id):
    data = request.get_json()
    datos_actualizados = grupo_mapping.load(data)
    grupo_actualizado = GrupoService.actualizar_grupo(id, datos_actualizados)
    if grupo_actualizado:
        return grupo_mapping.dump(grupo_actualizado), 200
    return jsonify({"message": "Grupo no encontrado"}), 404


@grupo_bp.route('/grupo/<hashid:id>', methods=['DELETE'])
def eliminar_grupo(id):
    grupo = GrupoService.borrar_por_id(id)
    if grupo:
        return jsonify({"message": "Grupo eliminado"}), 200
    return jsonify({"message": "Grupo no encontrado"}), 404