from dataclasses import dataclass
from app import db

@dataclass
class Pagos(db.Model):
    __tablename__ = 'Pagos'

    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    producto_id: int = db.Column('producto_id', db.Integer, db.ForeignKey('producto.id'), nullable=False)
    precio: int = db.Column('precio', db.Integer, nullable=False)
    medio_pago: str = db.Column('medio_pago', db.Text, nullable=False)

    # Relaciones
    producto = db.relationship('Producto', backref='pagos', lazy=True)
