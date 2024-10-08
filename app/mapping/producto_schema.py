from marshmallow import fields, Schema, post_load, validate
from app.models import Producto

class ProductoSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=8, max=40))
    precio = fields.Float(nullable=False)
    activado = fields.Boolean(nullable=False)
    
    @post_load
    def make_producto(self, data, **kwargs):
        return Producto(**data)