from flask import request, jsonify
from flask_restful import Resource

from repositories import LogStockRepository

class LogStock(Resource):

    def get(self):
        # TODO: error handler
        # move to another resource
        data = LogStockRepository.findAll()
        return data, 200

class LogStockByProductId(Resource):
    def get(self, product_id):
        # TODO: error handler
        # move to another resource
        data = LogStockRepository.findByProductId(product_id)
        return data, 200
