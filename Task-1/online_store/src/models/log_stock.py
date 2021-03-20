from . import db
from .base import BaseModel

import datetime


class LogStock(db.Model, BaseModel):
    id = db.Column(
        db.BigInteger, db.Sequence('log_stock_id_seq'), primary_key=True,
        unique=True, nullable=False)
    stock = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    remark = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, stock, product_id, remark):
        self.stock = stock
        self.product_id = product_id
        self.remark = remark
