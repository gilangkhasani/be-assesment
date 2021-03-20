from sqlalchemy.exc import IntegrityError
from exceptions import ResourceExists
from models import Checkout, Stock, Cart, db
from repositories import LogStockRepository


class CheckoutRepository:

    @staticmethod
    def findAll() -> dict:
        """ Get All Checkout """
        data: dict = {}
        data = Checkout.query.all()
        data_list = []
        for res in data:
            data = {
                'id' : res.id,
                'cart_id': res.cart_id,
                'date_created': str(res.date_created),
            }
            data_list.append(data)
        
        return data_list

    @staticmethod
    def create(cart_number) -> dict:
        """ Create Checkout """
        result: dict = {}
        try:
            data_cart = Cart.query.filter_by(cart_number = cart_number).all()
            result_messages = []
            for res_cart in data_cart:
                data_stock = Stock.query.filter_by(product_id=res_cart.product_id).first()
                if(data_stock is not None and data_stock.stock > 0):
                    if ((data_stock.stock - res_cart.qty) >= 0):
                        current_stock = data_stock.stock - res_cart.qty
                        data_stock.stock = current_stock
                        remark = "Stock Decreased from " + str(data_stock.stock) + " to " + str(current_stock)
                        data_stock.commit()
                        result = {
                            'product_id' : res_cart.product_id,
                            'message' : remark
                        }
                        LogStockRepository.create(current_stock, res_cart.product_id, remark)
                    else :
                        result = {
                            'product_id' : res_cart.product_id,
                            'message' : 'Stock is not Enough'
                        }
                else :
                    result = {
                        'product_id' : res_cart.product_id,
                        'message' : 'Stock Unavailable'
                    }
                result_messages.append(result)
            data = Checkout(cart_number)
            data.save()
            result = {
                'cart_number': cart_number,
                'date_created': str(data.date_created),
                'message' : result_messages
            }
        except IntegrityError:
            Checkout.rollback()
            raise ResourceExists('file_name already exists')

        return result

    
    @staticmethod
    def findByCartId(cart_id) -> dict:
        """ Query a Checkout by name """
        data: dict = {}
        data = Checkout.query.filter_by(cart_id=cart_id).first_or_404()
        data = {
            'id' : data.id,
            'cart_id': data.cart_id,
            'date_created': str(data.date_created),
        }
        
        return data

    @staticmethod
    def findById(id) -> dict:
        """ Query a Checkout by id """
        data: dict = {}
        data = Checkout.query.filter_by(id=id).first_or_404()
        data = {
            'id' : id,
            'cart_id': data.cart_id,
            'date_created': str(data.date_created),
        }
        
        return data

    @staticmethod
    def deleteById(id) -> dict:
        """ Query a Checkout by id """
        data: dict = {}
        data = Checkout.query.filter_by(id=id).delete()
        db.session.commit()
        data = {
          'status': 'Deleted ' ,
        }
        return data
