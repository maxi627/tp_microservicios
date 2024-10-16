from dataclasses import dataclass
from app import db
from datetime import datetime

@dataclass
class Stock(db.Model):
    __tablename__ = 'stock'

    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    producto_id: int = db.Column('producto_id', db.Integer, db.ForeignKey('producto.id'), nullable=False)
    fecha_transaccion: datetime = db.Column('fecha_transaccion', db.DateTime, nullable=False)
    cantidad: float = db.Column('cantidad', db.Float, nullable=False)
    entrada_salida: int = db.Column('entrada_salida', db.Integer, nullable=False)  # 1: entrada, 2: salida
