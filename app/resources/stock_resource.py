from flask import Flask, jsonify, request
from models import db, Stock

app = Flask(__name__)

@app.route('/stock', methods=['POST'])
def actualizar_stock():
    data = request.get_json()
    nuevo_stock = Stock(producto_id=data['producto_id'], cantidad=data['cantidad'], tipo=data['tipo'])
    db.session.add(nuevo_stock)
    db.session.commit()
    return jsonify({'producto_id': nuevo_stock.producto_id, 'cantidad': nuevo_stock.cantidad, 'tipo': nuevo_stock.tipo}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
