
import os
from dotenv import load_dotenv

# Cargar variables de entorno globales
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))

# Definir la versión del proyecto
__version__ = "1.0.0"
