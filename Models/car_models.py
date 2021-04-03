from app import db

class Cars(db.Model):
    __tablename__ = 'cars_model'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())
    make = db.Column(db.String())
    year = db.Column(db.Integer())
    price = db.Column(db.Integer())
    mileage = db.Column(db.Integer())

    def __init__(self, title, model, doors, make, year, price, mileage):
        self.title = title
        self.model = model
        self.doors = doors
        self.make = make
        self.year = year
        self.price = price
        self.mileage = mileage

    def __repr__(self):
        return f"<Car {self.title}>"