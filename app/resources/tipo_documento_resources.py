from flask import jsonify, Blueprint, request
from app.services.tipo_doc_service import TipoDocumentoService
from app.mapping.tipo_documento_mapping import TipoDocumentoMapping

tipo_doc_bp = Blueprint('tipo_doc', __name__)
tipo_doc_mapping = TipoDocumentoMapping()


@tipo_doc_bp.route('/tipos_documento', methods=['GET'])
def buscar_tipos_documento():
    tipos_doc = TipoDocumentoService.buscar_todos_doc()
    return tipo_doc_mapping.dump(tipos_doc, many=True), 200


@tipo_doc_bp.route('/tipos_documento/<hashid:id>', methods=['GET'])
def buscar_tipo_documento_id(id):
    tipo_doc = TipoDocumentoService.buscar_documento_id(id)
    if tipo_doc:
        return tipo_doc_mapping.dump(tipo_doc), 200
    return jsonify({"message": "Tipo de documento no encontrado"}), 404


@tipo_doc_bp.route('/tipos_documento', methods=['POST'])
def crear_tipo_documento():
    data = request.get_json()
    tipo_doc = tipo_doc_mapping.load(data)
    TipoDocumentoService.crear_tipo_documento(tipo_doc)
    return tipo_doc_mapping.dump(tipo_doc), 201


@tipo_doc_bp.route('/tipos_documento/<hashid:id>', methods=['PUT'])
def actualizar_tipo_documento(id):
    data = request.get_json()
    datos_actualizados = tipo_doc_mapping.load(data)
    tipo_doc_actualizado = TipoDocumentoService.actualizar_tipo_documento(datos_actualizados)
    if tipo_doc_actualizado:
        return tipo_doc_mapping.dump(tipo_doc_actualizado), 200
    return jsonify({"message": "Tipo de documento no encontrado"}), 404 


@tipo_doc_bp.route('/tipos_documento/<hashid:id>', methods=['DELETE'])
def eliminar_tipo_documento(id):
    tipo_doc = TipoDocumentoService.borrar_tipo_documento_id(id)
    if tipo_doc:
        return jsonify({"message": "Tipo de documento eliminado"}), 200
    return jsonify({"message": "Tipo de documento no encontrado"}), 404