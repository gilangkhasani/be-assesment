from . import db
from .base import BaseModel

import datetime


class Stock(db.Model, BaseModel):
    id = db.Column(
        db.BigInteger, db.Sequence('stock_id_seq'), primary_key=True,
        unique=True, nullable=False)
    stock = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, stock, product_id):
        self.stock = stock
        self.product_id = product_id
