from flask import Blueprint, render_template, \
    redirect, request, url_for, flash
from flask_security import current_user
from models import Item, City, Delivery, Payment

from ...forms import OrderForm
from .task import get_order

item = Blueprint("item", __name__)


@item.route("/<string:name>", methods=["GET", "POST"])
def item_detail(name):
    item = Item.query.filter(Item.item_name == name).first()
    return render_template("item/detail.html", item=item)


@item.route("/order/<string:name>", methods=["GET", "POST"])
def order_item(name):
    item = Item.query.filter(Item.item_name == name).first()
    form = OrderForm()

    if request.method == "POST":
        order_info = {"name": form.name.data, "surname": form.surname.data, "phone": form.phone.data,
                      "item": item.item_name, "city": form.city.data, "delivery_type": form.delivery.data,
                      "payment": form.payment.data, "comments": form.comments.data, "price": item.price}
        get_order.delay(order_info)
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
