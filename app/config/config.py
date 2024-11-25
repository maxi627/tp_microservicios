import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "../.env"))  # Carga las variables del entorno

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URI", "postgresql://maxi:1234@db:5432/dev_db")

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("PROD_DATABASE_URI", "postgresql://maxi:password@db:5432/prod_db")

def factory(env):
    envs = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
    }
    return envs.get(env, DevelopmentConfig)
