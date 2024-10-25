from flask import Flask, jsonify, request
from models import db, Compra

app = Flask(__name__)

@app.route('/compras', methods=['POST'])
def realizar_compra():
    data = request.get_json()
    nueva_compra = Compra(producto_id=data['producto_id'], cantidad=data['cantidad'])
    db.session.add(nueva_compra)
    db.session.commit()
    return jsonify({'id': nueva_compra.id, 'producto_id': nueva_compra.producto_id, 'cantidad': nueva_compra.cantidad}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
