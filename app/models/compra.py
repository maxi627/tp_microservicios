from dataclasses import dataclass
from app import db
from sqlalchemy import DateTime

@dataclass
class Categoria(db.Model):
    __tablename__ = 'Compra'

    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    producto: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    fecha_compra: DateTime = db.Column('fecha_compra', db.DateTime, nullable=False)
    direccion_envio: str = db.Column('nombre', db.Text, nullable=False)


#relaciones...
###
##
#


