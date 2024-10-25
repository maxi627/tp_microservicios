from flask import Flask, jsonify
from models import Producto 

app = Flask(__name__)

@app.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.filter_by(id=id, activo=True).first()
    if producto:
        return jsonify({
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': producto.precio
        }), 200
    return jsonify({'error': 'Producto no encontrado'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
