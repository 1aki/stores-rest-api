from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # lazy='dynamic': do not go into itemmodel and create object for each items YET
    items = db.relationship('ItemModel', lazy='dynamic') # Many to one. This is a list of many items.

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.items.all()]} # retrieves all the items for the store here rather than at line 11.

    # Returns an object, so should stay a classmethod unlike insert and update (save_to_db)
    @classmethod
    def find_by_name(cls, name):
        return StoreModel.query.filter_by(name=name).first()  # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        # SQLAlchemy automatically does update rather than insert. Ideal for both insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()