from flask import jsonify, Blueprint, request
from app.services import PlanService
from app.mapping.plan_mapping import PlanMapping

plan_bp = Blueprint('plan', __name__)
plan_mapping = PlanMapping()

@plan_bp.route('/plan', methods=['GET'])
def buscar_todos():
    planes = PlanService.buscar_todos()
    return plan_mapping.dump(planes, many=True), 200

@plan_bp.route('/plan/<hashid:id>', methods=['GET'])
def buscar_plan_id(id):
    plan = PlanService.buscar_por_id(id)
    if plan:
        return plan_mapping.dump(plan), 200
    return jsonify({"message": "Plan no encontrado"}), 404

@plan_bp.route('/plan', methods=['POST'])
def crear_plan():
    data = request.get_json()
    plan = plan_mapping.load(data)
    PlanService.crear_plan(plan)
    return plan_mapping.dump(plan), 201

@plan_bp.route('/plan/<hashid:id>', methods=['PUT'])
def actualizar_plan(id):
    data = request.get_json()
    datos_actualizados = plan_mapping.load(data)
    plan_actualizado = PlanService.actualizar_plan(
        id, datos_actualizados)
    if plan_actualizado:
        return plan_mapping.dump(plan_actualizado), 200
    return jsonify({"message": "Plan no encontrado"}), 404

@plan_bp.route('/plan/<hashid:id>', methods=['DELETE'])
def eliminar_plan(id):
    plan = PlanService.borrar_por_id(id)
    if plan:
        return jsonify({"message": "Plan eliminado"}), 200
    return jsonify({"message": "Plan no encontrado"}), 404