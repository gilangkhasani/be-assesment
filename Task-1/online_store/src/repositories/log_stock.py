from sqlalchemy.exc import IntegrityError
from exceptions import ResourceExists
from models import LogStock, db


class LogStockRepository:

    @staticmethod
    def findAll() -> dict:
        """ Get All LogStock """
        data: dict = {}
        data = LogStock.query.all()
        data_list = []
        for res in data:
            data = {
                'id' : res.id,
                'product_id': res.product_id,
                'stock': res.stock,
                'remark': data.remark,
                'date_created': str(res.date_created),
            }
            data_list.append(data)
        
        return data_list

    @staticmethod
    def create(stock, product_id, remark) -> dict:
        """ Create LogStock """
        result: dict = {}
        try:
            data = LogStock(stock, product_id, remark)
            data.save()
            result = {
                'product_id': data.product_id,
                'stock': data.stock,
                'remark': data.remark,
                'date_created': str(data.date_created),
            }
        except IntegrityError:
            LogStock.rollback()
            raise ResourceExists('file_name already exists')

        return result

    @staticmethod
    def findByProductId(product_id) -> dict:
        """ Query a LogStock by name """
        data: dict = {}
        data = LogStock.query.filter_by(product_id=product_id).first_or_404()
        data = {
            'id' : id,
            'stock': data.stock,
            'product_id': data.product_id,
            'remark': data.remark,
            'date_created': str(data.date_created),
        }
        
        return data

    @staticmethod
    def deleteById(id) -> dict:
        """ Query a LogStock by id """
        data: dict = {}
        data = LogStock.query.filter_by(id=id).delete()
        db.session.commit()
        data = {
          'status': 'Deleted ' ,
        }
        return data
