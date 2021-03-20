from . import db
from .base import BaseModel

import datetime


class User(db.Model, BaseModel):
    username = db.Column(
        db.String, primary_key=True,
        unique=True, nullable=False)
    avatar_url = db.Column(db.String, nullable=True)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username, first_name, last_name, avatar_url):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.avatar_url = avatar_url
