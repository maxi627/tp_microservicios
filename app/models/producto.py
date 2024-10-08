from dataclasses import dataclass
from app import db

@dataclass
class Producto(db.Model):
    __tablename__ = 'producto'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nambre: str = db.Column('nambre', db.String, primary_key=True, autoincrement=True)
    precio: float = db.Column('precio',db.Float, nullable=False)
    activado: bool = db.Column('activado', db.Boolean, nullable=False)
