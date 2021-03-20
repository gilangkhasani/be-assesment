from flask import request, jsonify
from flask_restful import Resource

from repositories import CartRepository

class Cart(Resource):

    def get(self):
        # TODO: error handler
        # move to another resource
        data = CartRepository.findAll()
        return data, 200

    def post(self):
        """
        Create Cart
        """
        request_json_list = request.get_json(silent=True)
        response_list = []
        cart_number = CartRepository.getCartNumber()
        for request_json in request_json_list:
            qty = request_json['qty']
            product_id = request_json['product_id']
            username = request_json['username']
            try:
                response = CartRepository.create(qty, product_id, username, cart_number)
                response_list.append(response)
                
            except Exception as e:
                response = jsonify(e.to_dict())
                response.status_code = e.status_code
                return response
            
        return request_json_list, 200

class CartByUsername(Resource):
    def get(self, username):
        # TODO: error handler
        # move to another resource
        data = CartRepository.findByUsername(username)
        return data, 200
