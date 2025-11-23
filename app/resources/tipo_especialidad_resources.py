from flask import jsonify, Blueprint, request
from app.services.tipo_especialidad_service import TipoEspecialidadService
from app.mapping.tipo_especialidad_mapping import TipoEspecialidadMapping

tipo_esp_bp = Blueprint('tipo_esp',__name__)
tipo_especialidad_mapping = TipoEspecialidadMapping()


@tipo_esp_bp.route('/tipo_especialidad', methods=['GET'])
def buscar_tipo_especialidades():
    tipos_especialidades = TipoEspecialidadService.buscar_todos()
    return tipo_especialidad_mapping.dump(tipos_especialidades, many=True), 200


@tipo_esp_bp.route('/tipo_especialidad/<hashid:id>', methods=['GET'])
def buscar_tipo_especialidad_por_id(id):
    tipo_especialidad = TipoEspecialidadService.buscar_por_id(id)
    if tipo_especialidad:
        return tipo_especialidad_mapping.dump(tipo_especialidad), 200
    return jsonify({"message": "Tipo de especialidad no encontrado"}), 404


@tipo_esp_bp.route('/tipo_especialidad', methods=['POST'])
def crear_tipo_especialidad():
    data = request.get_json()
    tipo_especialidad = tipo_especialidad_mapping.load(data)
    nuevo_tipo_especialidad = TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
    return tipo_especialidad_mapping.dump(nuevo_tipo_especialidad), 201


@tipo_esp_bp.route('/tipo_especialidad/<hashid:id>', methods=['PUT'])
def actualizar_tipo_especialidad(id):
    data = request.get_json()
    datos_actualizados = tipo_especialidad_mapping.load(data)
    tipo_especialidad_actualizado = TipoEspecialidadService.actualizar_tipo_especialidad(id, datos_actualizados)
    if tipo_especialidad_actualizado:
        return tipo_especialidad_mapping.dump(tipo_especialidad_actualizado), 200
    return jsonify({"message": "Tipo de especialidad no encontrado"}), 404


@tipo_esp_bp.route('/tipo_especialidad/<hashid:id>', methods=['DELETE'])
def eliminar_tipo_especialidad(id):
    eliminado = TipoEspecialidadService.borrar_por_id(id)
    if eliminado:
        return jsonify({"message": "Tipo de especialidad eliminado exitosamente"}), 200
    return jsonify({"message": "Tipo de especialidad no encontrado"}), 404