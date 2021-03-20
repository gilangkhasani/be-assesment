from . import db
from .base import BaseModel

import datetime


class Cart(db.Model, BaseModel):
    id = db.Column(
        db.BigInteger, db.Sequence('cart_id_seq'), primary_key=True,
        unique=True, nullable=False)
    qty = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    username = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)
    cart_status = db.Column(db.String(50))
    cart_number = db.Column(db.String(15))
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, qty, product_id, username, cart_status, cart_number):
        self.qty = qty
        self.product_id = product_id
        self.username = username
        self.cart_status = cart_status
        self.cart_number = cart_number
