from flask import request, jsonify
from flask_restful import Resource

from repositories import StockRepository, LogStockRepository

class Stock(Resource):

    def get(self):
        # TODO: error handler
        # move to another resource
        data = StockRepository.findAll()
        return data, 200

    def post(self):
        """
        Create Stock
        """
        request_json = request.get_json(silent=True)
        product_id = request_json['product_id']
        stock = request_json['stock']
        remark = request_json['remark']
        
        try:
            response = StockRepository.create(stock, product_id)
            LogStockRepository.create(stock, product_id, remark)
            return response, 200
        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response

class StockByProductId(Resource):
    def get(self, product_id):
        # TODO: error handler
        # move to another resource
        data = StockRepository.findByProductId(product_id)
        return data, 200
