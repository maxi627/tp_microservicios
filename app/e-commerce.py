# app/e_commerce.py
import requests

def obtener_producto(id_producto):
    url = f"http://ms-producto:5004/productos/{id_producto}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def realizar_compra(producto_id, cantidad):
    url = "http://ms-compras:5003/compras"
    data = {'producto_id': producto_id, 'cantidad': cantidad}
    response = requests.post(url, json=data)
    return response.json() if response.status_code == 201 else None

def realizar_pago(compra_id, monto):
    url = "http://ms-pagos:5001/pagos"
    data = {'compra_id': compra_id, 'monto': monto}
    response = requests.post(url, json=data)
    return response.json() if response.status_code == 201 else None

def actualizar_stock(producto_id, cantidad):
    url = "http://ms-stock:5003/stock"
    data = {'producto_id': producto_id, 'cantidad': cantidad, 'tipo': 'salida'}
    response = requests.post(url, json=data)
    return response.json() if response.status_code == 200 else None

def proceso_compra(id_producto, cantidad):
    producto = obtener_producto(id_producto)
    if not producto:
        return "Producto no encontrado"
    
    compra = realizar_compra(producto['id'], cantidad)
    if not compra:
        return "Error al realizar la compra"
    
    pago = realizar_pago(compra['id'], producto['precio'] * cantidad)
    if not pago:
        return "Error al realizar el pago"
    
    stock = actualizar_stock(producto['id'], cantidad)
    if not stock:
        return "Error al actualizar el stock"
    
    return "Compra realizada con éxito"

# Simulación de la compra
resultado = proceso_compra(1, 2)
print(resultado)
