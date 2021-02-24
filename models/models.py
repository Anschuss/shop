from .database import db
from login import login
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), unique=True)
    phone_number = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(120))
    item = db.Column(db.ARRAY(db.Integer))

    def __repr__(self):
        return f"User: {self.name}, {self.email}, {self.phone_number}"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(120),
                    default="https://images.squarespace-cdn.com/content/v1/5b275e8b45776eccb6c16312/1569840334525-XJP98CCM5K84EJSBYBJ1/ke17ZwdGBToddI8pDm48kPoswlzjSVMM-SxOp7CV59BZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZamWLI2zvYWH8K3-s_4yszcp2ryTI0HqTOaaUohrI8PI6FXy8c9PWtBlqAVlUS5izpdcIXDZqDYvprRqZ29Pw0o/obst-shop.gif?format=750w")
    item_name = db.Column(db.String(120), unique=True, nullable=False)
    intro = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"Item: {self.name}, {self.intro}, {self.price}"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(32), nullable=False)
    customer_surname = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    item = db.Column(db.String(32))
    order_city = db.Column(db.String(32), db.ForeignKey("city.city_name"))
    delivery_type = db.Column(db.String(32), db.ForeignKey("delivery.delivery_type"))
    payment_method = db.Column(db.String(32), db.ForeignKey("payment.method"))
    comments = db.Column(db.Text)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"Order: {self.username}, {self.items}, {self.comments}, {self.price}"


class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(64), unique=True)

    order = db.relationship(Order, backref="city")

    def __repr__(self):
        return f"City: {self.id}, {self.city_name}"


class Delivery(db.Model):
    __tablename__ = "delivery"
    id = db.Column(db.Integer, primary_key=True)
    delivery_type = db.Column(db.String(32), unique=True)
    price = db.Column(db.Integer)

    order = db.relationship(Order, backref="delivery")


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(64), unique=True)

    order = db.relationship(Order, backref="payment")
