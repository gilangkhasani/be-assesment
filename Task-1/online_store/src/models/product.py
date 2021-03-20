from . import db
from .base import BaseModel

import datetime


class Product(db.Model, BaseModel):
    id = db.Column(
        db.BigInteger, db.Sequence('product_id_seq'), primary_key=True,
        unique=True, nullable=False)
    name = db.Column(db.String(255))
    desc = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
