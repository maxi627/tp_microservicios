from marshmallow import fields, Schema, post_load, validate
from compra.models import Compra

class CompraSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(dump_only=True)
    fecha_compra = fields.DateTime(required=True)  
    direccion_envio = fields.String(required=True, validate=validate.Length(min=8, max=40))

    @post_load
    def make_compra(self, data, **kwargs):
        return Compra(**data)
