from flask import jsonify, Blueprint, request
from app.mapping import StockSchema
from app.services import StockService

stock = Blueprint('stock', __name__)
service = StockService()
stock_schema = StockSchema()

"""
Obtiene todas las stocks
"""
@stock.route('/stocks', methods=['GET'])
def all():
    resp = stock_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene un stock por id
"""
@stock.route('/stocks/<int:id>', methods=['GET'])
def one(id):
    resp = stock_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea un nuevo stock
"""
@stock.route('/stocks', methods=['POST'])
def create():
    stock = stock_schema.load(request.json)
    resp = stock_schema.dump(service.create(stock))
    return resp, 201

"""
Actualiza un stock existente
"""
@stock.route('/stocks/<int:id>', methods=['PUT'])
def update(id):
    stock = stock_schema.load(request.json)
    resp = stock_schema.dump(service.update(id, stock))
    return resp, 200

"""
Elimina un stock existente
"""
@stock.route('/stocks/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "stock eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar la stock"
    return jsonify(msg), 204