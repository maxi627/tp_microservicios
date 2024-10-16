from dataclasses import dataclass
from app import db
from sqlalchemy import DateTime

@dataclass
class Compra(db.Model):
    __tablename__ = 'Compra'

    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    producto_id: int = db.Column('producto_id', db.Integer, db.ForeignKey('producto.id'), nullable=False)
    fecha_compra: DateTime = db.Column('fecha_compra', db.DateTime, nullable=False)
    direccion_envio: str = db.Column('direccion_envio', db.Text, nullable=False)

 
