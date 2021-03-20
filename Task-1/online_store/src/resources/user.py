from flask import request, jsonify
from flask_restful import Resource

from repositories import UserRepository


class User(Resource):
    def get(self, username: str):
        # TODO: error handler
        # move to another resource
        user = UserRepository.findByUsername(username)
        return user, 200


class UserList(Resource):
    def post(self):
        """
        Create user
        """
        request_json = request.get_json(silent=True)
        username: str = request_json['username']
        first_name: str = request_json['first_name']
        last_name: str = request_json['last_name']
        avatar_url: str = request_json.get('avatar_url', '')
        try:
            user = UserRepository.create(username, first_name, last_name, avatar_url)
            return user, 200
        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
