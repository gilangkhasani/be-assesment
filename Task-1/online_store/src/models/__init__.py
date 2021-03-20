# flake8: noqa
# TODO: check if there is a better way
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .base import BaseModel
from .user import User
from .product import Product
from .stock import Stock
from .log_stock import LogStock
from .cart import Cart
from .checkout import Checkout

__all__ = ['BaseModel', 'User', 'Product', 'Stock', 'LogStock', 'Cart', 'Checkout']
