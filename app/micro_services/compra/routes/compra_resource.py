from flask import Blueprint, jsonify, request
from app.micro_services.compra.mapping import CompraSchema
from app.micro_services.compra.services import CompraService

compra = Blueprint('compra', __name__)
service = CompraService()
compra_schema =CompraSchema()

"""
Obtiene todos las compras
"""
@compra.route('/compras', methods=['GET'])
def all():
    resp = compra_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una compra por id
"""
@compra.route('/compras/<int:id>', methods=['GET'])
def one(id):
    resp = compra_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva compra
"""
@compra.route('/compras', methods=['POST'])
def create():
    compra = compra_schema.load(request.json)
    resp = compra_schema.dump(service.create(compra))
    return resp, 201

"""
Actualiza una compra existente
"""
@compra.route('/compras/<int:id>', methods=['PUT'])
def update(id):
    compra = compra_schema.load(request.json)
    resp = compra_schema.dump(service.update(id, compra))
    return resp, 200

"""
Elimina una compra existente
"""
@compra.route('/compras/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "compra eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el compra"
    return jsonify(msg), 204