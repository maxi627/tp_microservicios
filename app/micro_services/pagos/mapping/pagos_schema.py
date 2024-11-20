from marshmallow import fields, Schema, post_load, validate
from pagos.models import Pagos

class PagosSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(dump_only=True)
    precio= fields.Float(nullable=False)
    medio_pago = fields.String(required=True, validate=validate.Length(min=8, max=40))

    @post_load
    def make_pagos(self, data, **kwargs):
        return Pagos(**data)
