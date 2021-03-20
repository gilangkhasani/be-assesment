from sqlalchemy.exc import IntegrityError
from exceptions import ResourceExists
from models import Stock, db


class StockRepository:

    @staticmethod
    def findAll() -> dict:
        """ Get All Stock """
        data: dict = {}
        data = Stock.query.all()
        data_list = []
        for res in data:
            data = {
                'id' : res.id,
                'product_id': res.product_id,
                'stock': res.stock,
                'date_created': str(res.date_created),
            }
            data_list.append(data)
        
        return data_list

    @staticmethod
    def create(stock, product_id) -> dict:
        """ Create Stock """
        result: dict = {}
        try:
            data = Stock.query.filter_by(product_id=product_id).first()
            if(data is None):
                data = Stock(stock, product_id)
                data.save()
            else :
                print(data)
                data.stock = stock
                data.commit()

            result = {
                'product_id': data.product_id,
                'stock': data.stock,
                'date_created': str(data.date_created),
            }
        except IntegrityError:
            Stock.rollback()
            raise ResourceExists('file_name already exists')

        return result

    @staticmethod
    def findByProductId(product_id) -> dict:
        """ Query a Stock by product_id """
        data: dict = {}
        data = Stock.query.filter_by(product_id=product_id).first_or_404()
        data = {
            'id' : data.id,
            'stock': data.stock,
            'product_id': data.product_id,
            'date_created': str(data.date_created),
        }
        return data

    @staticmethod
    def deleteById(id) -> dict:
        """ Query a Stock by id """
        data: dict = {}
        data = Stock.query.filter_by(id=id).delete()
        db.session.commit()
        data = {
          'status': 'Deleted ' ,
        }
        return data
