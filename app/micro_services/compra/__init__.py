import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config.config import factory

db = SQLAlchemy()

def create_app():
    # Crear la app de Flask
    app = Flask(__name__)

    # Configuración desde el entorno
    app_context = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(factory(app_context))

    # Inicializar extensiones
    db.init_app(app)
    # cache.init_app(app, config=cache_config)

    # Registrar Blueprints
    from compra.routes import compra_bp
    app.register_blueprint(compra_bp, url_prefix='/api/v1/compras')

    # Ruta de prueba para la salud del servicio
    @app.route('/ping', methods=['GET'])
    def ping():
        return {"message": "El servicio de compras está en funcionamiento"}

    return app

