from flask import Blueprint, render_template, \
    redirect, request, url_for, flash
from flask_login import current_user
from models import db, Item, Order, City, Delivery, Payment

from ...forms import OrderForm

item = Blueprint("item", __name__)


@item.route("/<string:name>", methods=["GET", "POST"])
def item_detail(name):
    item = Item.query.filter(Item.name == name).first()
    return render_template("item/detail.html", item=item)

def get_price(item_price, delivery_type):
    delivery = Delivery.query.filter(Delivery.delivery_type == delivery_type).first()
    price = item_price + delivery.price
    return price

@item.route("/order/<string:name>", methods=["GET", "POST"])
def order_item(name):
    item = Item.query.filter(Item.name == name).first()
    form = OrderForm()

    if request.method == "POST":
        order = Order(name=form.name.data, surname=form.surname.data, phone=form.phone.data, item=name,
                      city_name=form.city.data, delivery_type=form.delivery.data,payment_method=form.payment.data,
                      comments=form.comments.data, price=get_price(item.price, form.delivery.data))
        db.session.add(order)
        db.session.commit()
        flash("Your order has been create!", "success")
        return redirect(url_for("general.general_page"))

    if current_user.is_authenticated:
        form.name.data = current_user.name
        form.surname.data = current_user.surname
        form.phone.data = current_user.phone_number

    form.city.choices = [city.city_name for city in City.query.all()]
    form.delivery.choices = [delivery.delivery_type for delivery in Delivery.query.all()]
    form.payment.choices = [payment.method for payment in Payment.query.all()]

    return render_template("item/order.html", form=form, item=item)
