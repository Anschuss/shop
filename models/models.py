from .database import db
from login import login


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(64), unique=True)
    phone_number = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(120))
    item = db.Column(db.ARRAY(db.Integer))

    order = db.relationship("Order", backref="customer")

    def __repr__(self):
        return f"User: {self.name}, {self.email}, {self.phone_number}"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(120), default="https://images.squarespace-cdn.com/content/v1/5b275e8b45776eccb6c16312/1569840334525-XJP98CCM5K84EJSBYBJ1/ke17ZwdGBToddI8pDm48kPoswlzjSVMM-SxOp7CV59BZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZamWLI2zvYWH8K3-s_4yszcp2ryTI0HqTOaaUohrI8PI6FXy8c9PWtBlqAVlUS5izpdcIXDZqDYvprRqZ29Pw0o/obst-shop.gif?format=750w")
    name = db.Column(db.String(120), unique=True, nullable=False)
    intro = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"Item: {self.name}, {self.intro}, {self.price}"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, db.ForeignKey("user.id"))
    items = db.Column(db.ARRAY(db.Integer))
    comments = db.Column(db.String(256))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"Order: {self.username}, {self.items}, {self.comments}, {self.price}"
