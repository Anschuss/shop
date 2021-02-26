from .database import db
from login import login
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), unique=True)
    phone_number = db.Column(db.BIGINT, unique=True)
    password = db.Column(db.String(120))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), default=1)

    order = db.relationship("Order", backref="user")

    def __repr__(self):
        return f"{self.email}"


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(32), unique=True)
    description = db.Column(db.Text)

    users = db.relationship(User, backref="role")

    def __repr__(self):
        return f"{self.role}"


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
        return f"Item: {self.item_name}, {self.intro}, {self.price}"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.BIGINT)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    item = db.Column(db.String(32))
    order_city = db.Column(db.String(32), db.ForeignKey("city.city_name"))
    delivery_type = db.Column(db.String(32), db.ForeignKey("delivery.delivery_type"))
    payment_method = db.Column(db.String(32), db.ForeignKey("payment.method"))
    comments = db.Column(db.Text)
    status = db.Column(db.Boolean, default=False)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.item}: {self.price}€, {self.status}"


class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(64), unique=True)

    order = db.relationship(Order, backref="city")

    def __repr__(self):
        return f"{self.city_name}"


class Delivery(db.Model):
    __tablename__ = "delivery"
    id = db.Column(db.Integer, primary_key=True)
    delivery_type = db.Column(db.String(32), unique=True)
    price = db.Column(db.Integer)

    order = db.relationship(Order, backref="delivery")

    def __repr__(self):
        return f"{self.delivery_type}"


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(64), unique=True)

    order = db.relationship(Order, backref="payment")

    def __repr__(self):
        return f"{self.method}"