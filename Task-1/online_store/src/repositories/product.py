from sqlalchemy.exc import IntegrityError
from exceptions import ResourceExists
from models import Product, db


class ProductRepository:

    @staticmethod
    def findAll() -> dict:
        """ Get All Product """
        data: dict = {}
        data = Product.query.all()
        data_list = []
        for res in data:
            data = {
                'id' : res.id,
                'name': res.name,
                'desc': res.desc,
                'date_created': str(res.date_created),
            }
            data_list.append(data)
        
        return data_list

    @staticmethod
    def create(name, desc) -> dict:
        """ Create Product """
        result: dict = {}
        try:
            data = Product(name=name, desc=desc)
            data.save()
            result = {
                'name': data.name,
                'desc': data.desc,
                'date_created': str(data.date_created),
            }
        except IntegrityError:
            Product.rollback()
            raise ResourceExists('file_name already exists')

        return result

    @staticmethod
    def findByName(name) -> dict:
        """ Query a product by name """
        data: dict = {}
        data = Product.query.filter_by(name=name).first_or_404()
        data = {
            'id' : id,
            'name': data.name,
            'desc': data.desc,
            'date_created': str(data.date_created),
        }
        
        return data

    @staticmethod
    def findById(id) -> dict:
        """ Query a product by id """
        data: dict = {}
        data = Product.query.filter_by(id=id).first_or_404()
        data = {
            'id' : id,
            'name': data.name,
            'desc': data.desc,
            'date_created': str(data.date_created),
        }
        
        return data

    @staticmethod
    def deleteById(id) -> dict:
        """ Query a product by id """
        data: dict = {}
        data = Product.query.filter_by(id=id).delete()
        db.session.commit()
        data = {
          'status': 'Deleted ' ,
        }
        return data
