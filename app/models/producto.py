from dataclasses import dataclass
from app import db

@dataclass
class Producto(db.Model):
    __tablename__ = 'producto'

    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column('nombre', db.String, nullable=False)  # Corregido de 'nambre' a 'nombre'
    precio: float = db.Column('precio', db.Float, nullable=False)
    activado: bool = db.Column('activado', db.Boolean, nullable=False)

    # Relaciones
    compras = db.relationship('Compra', backref='producto', lazy=True)
    pagos = db.relationship('Pagos', backref='producto', lazy=True)
    stocks = db.relationship('Stock', backref='producto', lazy=True)
