from . import db


class BaseModel:
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @staticmethod
    def rollback():
        db.session.rollback()

    @staticmethod
    def commit():
        db.session.commit()
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
