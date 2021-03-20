from flask_restful import Api
from resources import HealthCheck, \
    UserList, User, Product, ProductById, StockByProductId, Stock, LogStockByProductId, Cart, CartByUsername, \
        Checkout
from models import User as UserModel, db, Product as ProductModel
from flask_migrate import Migrate
from app import create_app


app = create_app()
migrate = Migrate(app, db)


# API
api = Api(app)
api.add_resource(UserList, '/api/user')
api.add_resource(User, '/api/user/<username>')

api.add_resource(ProductById, '/api/product/<id>')
api.add_resource(Product, '/api/product')

api.add_resource(StockByProductId, '/api/stock/<product_id>')
api.add_resource(Stock, '/api/stock')

api.add_resource(LogStockByProductId, '/api/log-stock/<product_id>')

api.add_resource(Cart, '/api/cart')
api.add_resource(CartByUsername, '/api/cart/<username>')

api.add_resource(Checkout, '/api/checkout')

# CLI for migrations
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=UserModel, Product=ProductModel)
