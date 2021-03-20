from sqlalchemy.exc import IntegrityError
from exceptions import ResourceExists
from models import User


class UserRepository:

    @staticmethod
    def create(username, first_name, last_name, avatar_url) -> dict:
        """ Create user """
        result: dict = {}
        try:
            user = User(username=username, first_name=first_name, last_name=last_name, avatar_url=avatar_url)
            user.save()
            result = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'avatar_url': user.avatar_url,
                'date_created': str(user.date_created),
            }
        except IntegrityError:
            User.rollback()
            raise ResourceExists('user already exists')

        return result

    @staticmethod
    def findByUsername(username) -> dict:
        """ Query a user by username """
        user: dict = {}
        user = User.query.filter_by(username=username).first_or_404()
        user = {
          'username': user.username,
          'date_created': str(user.date_created),
        }
        return user
