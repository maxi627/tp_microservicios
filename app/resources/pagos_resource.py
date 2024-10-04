from flask import jsonify, Blueprint, request
from app.mapping import PagosSchema
from app.services import PagosService

pagos = Blueprint('pagos', __name__)
service = PagosService()
pagos_schema = PagosSchema()

"""
Obtiene todas los pagos
"""
@pagos.route('/pagos', methods=['GET'])
def all():
    resp = pagos_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene un pago por id
"""
@pagos.route('/pagos/<int:id>', methods=['GET'])
def one(id):
    resp = pagos_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea un nuevo pago
"""
@pagos.route('/pagos', methods=['POST'])
def create():
    pagos = pagos_schema.load(request.json)
    resp = pagos_schema.dump(service.create(pagos))
    return resp, 201

"""
Actualiza un pago existente
"""
@pagos.route('/pagos/<int:id>', methods=['PUT'])
def update(id):
    pagos = pagos_schema.load(request.json)
    resp = pagos_schema.dump(service.update(id, pagos))
    return resp, 200

"""
Elimina un pago existente
"""
@pagos.route('/pagos/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "pagos eliminados correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar los pagos"
    return jsonify(msg), 204