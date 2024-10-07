import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .config import config


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app() -> None:
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)
    f.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
    from app.resources import home, categoria, orden, producto, user
    app.register_blueprint(home, url_prefix='/api/v1')
    app.register_blueprint(user, url_prefix='/api/v1')
    app.register_blueprint(orden, url_prefix='/api/v1')
    app.register_blueprint(producto, url_prefix='/api/v1')
    app.register_blueprint(categoria, url_prefix='/api/v1')

   
    @app.shell_context_processor    
    def ctx():
        return {
            "app": app,
            'db' : db
            }
    
    return app
