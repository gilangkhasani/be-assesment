from flask import request, jsonify
from flask_restful import Resource

from repositories import ProductRepository

class Product(Resource):

    def get(self):
        # TODO: error handler
        # move to another resource
        data = ProductRepository.findAll()
        return data, 200

    def post(self):
        """
        Create Product
        """
        request_json = request.get_json(silent=True)
        name: str = request_json['name']
        desc: str = request_json['desc']
        
        try:
            response = ProductRepository.create(name, desc)
            return response, 200
        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response

class ProductById(Resource):
    def get(self, id):
        # TODO: error handler
        # move to another resource
        data = ProductRepository.findById(id)
        return data, 200
