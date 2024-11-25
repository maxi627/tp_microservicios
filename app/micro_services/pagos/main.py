from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

#Configuración de la conexión a la base de datos usando variables de entorno
DATABASE_USER = os.getenv("POSTGRES_USER")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_HOST = os.getenv("POSTGRES_HOST")
DATABASE_PORT = os.getenv("POSTGRES_PORT")
DATABASE_NAME = os.getenv("POSTGRES_DB")

# Función para conectar a la base de datos
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DATABASE_HOST,
            database=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            port=DATABASE_PORT
        )
        return conn
    except psycopg2.OperationalError as e:
        app.logger.error(f"Error de conexión a la base de datos: {e}")
        return None


# Endpoint para obtener todos los productos
@app.route('/productos', methods=['GET'])
def get_productos():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "No se pudo conectar a la base de datos."}), 500
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos;")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convertir los productos en un formato JSON
    if not productos:
        return jsonify([])  # Devuelve una lista vacía si no hay productos

    productos_list = [{"id": p[0], "nombre": p[1], "precio": p[2]} for p in productos]
    return jsonify(productos_list)

# Ruta de prueba para verificar la conexión
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "El servicio de stock está en funcionamiento"})

# Inicio del servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
