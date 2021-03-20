from . import db
from .base import BaseModel

import datetime


class Checkout(db.Model, BaseModel):
    id = db.Column(
        db.BigInteger, db.Sequence('checkout_id_seq'), primary_key=True,
        unique=True, nullable=False)
    cart_number = db.Column(db.String(15), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, cart_number):
        self.cart_number = cart_number
