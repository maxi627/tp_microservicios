from dataclasses import dataclass
from app import db

@dataclass
class Producto(db.Model):
    __tablename__ = 'producto'

    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column('nombre', db.String, nullable=False) 
    precio: float = db.Column('precio', db.Float, nullable=False)
    activado: bool = db.Column('activado', db.Boolean, nullable=False)
