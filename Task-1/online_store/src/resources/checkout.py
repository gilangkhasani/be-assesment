from flask import request, jsonify
from flask_restful import Resource

from repositories import CheckoutRepository

class Checkout(Resource):

    def get(self):
        # TODO: error handler
        # move to another resource
        data = CheckoutRepository.findAll()
        return data, 200

    def post(self):
        """
        Create Checkout
        """
        request_json = request.get_json(silent=True)
        cart_number = request_json['cart_number']
        
        try:
            response = CheckoutRepository.create(cart_number)
            return response, 200
        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
