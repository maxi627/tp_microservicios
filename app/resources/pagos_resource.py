from flask import Flask, jsonify, request
from models import db, Pago

app = Flask(__name__)

@app.route('/pagos', methods=['POST'])
def realizar_pago():
    data = request.get_json()
    nuevo_pago = Pago(compra_id=data['compra_id'], monto=data['monto'])
    db.session.add(nuevo_pago)
    db.session.commit()
    return jsonify({'id': nuevo_pago.id, 'compra_id': nuevo_pago.compra_id, 'monto': nuevo_pago.monto}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
