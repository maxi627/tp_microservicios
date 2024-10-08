from marshmallow import fields, Schema, post_load, validate
from app.models import Stock

class StockSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto = fields.String(required=True, validate=validate.Length(min=8, max=40))
    fecha_transaccion = fields.DateTime(nullable=False)
    cantidad = fields.Float(nullable=False)
    entrada_salida = fields.Integer(nullable=False)
    
    @post_load
    def make_stock(self, data, **kwargs):
        return Stock(**data)