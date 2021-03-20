from sqlalchemy.exc import IntegrityError
from exceptions import ResourceExists
from models import Cart, Stock, db
from datetime import datetime


class CartRepository:

    @staticmethod
    def findAll() -> dict:
        """ Get All Cart """
        data: dict = {}
        data = Cart.query.all()
        data_list = []
        for res in data:
            data = {
                'id' : res.id,
                'product_id': res.product_id,
                'qty': res.qty,
                'username': data.username,
                'date_created': str(res.date_created),
            }
            data_list.append(data)
        
        return data_list

    @staticmethod
    def create(qty, product_id, username, cart_number) -> dict:
        """ Create Cart """
        result: dict = {}
        try:
            data_stock = Stock.query.filter_by(product_id=product_id).first()
            if(data_stock is not None and data_stock.stock > 0):
                if ((data_stock.stock - qty) >= 0):
                    data = Cart(qty, product_id, username, 'Stock Available', cart_number)
                    data.save()
                    result = {
                        'product_id': data.product_id,
                        'qty': data.qty,
                        'username': data.username,
                        'date_created': str(data.date_created),
                    }
                else :
                    result = {
                        'message' : 'Stock is not Enough'
                    }
            else :
                result = {
                    'message' : 'Stock Unavailable'
                }
        except IntegrityError:
            Cart.rollback()
            raise ResourceExists('file_name already exists')

        return result

    @staticmethod
    def findByUsername(username) -> dict:
        """ Query a Cart by username """
        data: dict = {}
        data = Cart.query.filter_by(username=username).all()
        data_list = []
        for res in data:
            data = {
                'id' : res.id,
                'qty': res.qty,
                'product_id': res.product_id,
                'username': res.username,
                'date_created': str(res.date_created),
            }
            data_list.append(data)
        
        return data_list

    @staticmethod
    def findByProductId(product_id) -> dict:
        """ Query a Cart by name """
        data: dict = {}
        data = Cart.query.filter_by(product_id=product_id).first_or_404()
        data = {
            'id' : id,
            'qty': data.qty,
            'product_id': data.product_id,
            'username': data.username,
            'date_created': str(data.date_created),
        }
        
        return data

    @staticmethod
    def getCartNumber() -> dict:
        """ Query a get latest cart number """
        curdate = datetime.today().strftime('%Y%m%d')
        sql = "select coalesce(max(cart_number), concat(to_char(current_date, 'YYYYMMDD'), '0')) as max_cart_number from cart where date(date_created) = CURRENT_DATE " 
        results = db.engine.execute(sql)
        value = 0
        value = int(results.first()[0][8:])
        print(value)
        value += 1
        cart_number = curdate + '' + str(value)
        return cart_number

    @staticmethod
    def findById(id) -> dict:
        """ Query a Cart by id """
        data: dict = {}
        data = Cart.query.filter_by(id=id).first_or_404()
        data = {
            'id' : id,
            'qty': data.qty,
            'product_id': data.product_id,
            'remark': data.remark,
            'date_created': str(data.date_created),
        }
        
        return data

    @staticmethod
    def deleteById(id) -> dict:
        """ Query a Cart by id """
        data: dict = {}
        data = Cart.query.filter_by(id=id).delete()
        db.session.commit()
        data = {
          'status': 'Deleted ' ,
        }
        return data
