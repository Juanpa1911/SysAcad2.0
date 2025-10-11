from flask import jsonify, Blueprint, request
from app.services.area_service import AreaService
from app.mapping.area_mapping import AreaMapping

area_bp = Blueprint('area', __name__)
area_mapping = AreaMapping()

@area_bp.route('/area', methods=['GET'])
def buscar_todas():
    areas = AreaService.buscar_todos()
    return area_mapping.dump(areas, many=True), 200

@area_bp.route('/area/<hashid:id>', methods=['GET'])
def buscar_area_id(id):
    area = AreaService.buscar_por_id(id)
    if area:
        return area_mapping.dump(area), 200
    return jsonify({"message": "Area no encontrada"}), 404

@area_bp.route('/area', methods=['POST'])
def crear_area():
    data = request.get_json()
    area = area_mapping.load(data)
    area = AreaService.crear_area(area)
    return area_mapping.dump(area), 201

@area_bp.route('/area/<hashid:id>', methods=['PUT'])
def actualizar_area(id):
    data = request.get_json()
    area = area_mapping.load(data)
    area = AreaService.actualizar_area(area, id)
    if area:
        return area_mapping.dump(area), 200
    return jsonify({"message": "Area no encontrada"}), 404

@area_bp.route('/area/<hashid:id>', methods=['DELETE'])
def eliminar_area(id):
    area = AreaService.borrar_por_id(id)
    if area:
        return jsonify({"message": "Area eliminada"}), 200
    return jsonify({"message": "Area no encontrada"}), 404

