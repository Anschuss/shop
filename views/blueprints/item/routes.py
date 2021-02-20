from flask import Blueprint, render_template, redirect

from models import Item

item = Blueprint("item", __name__)


@item.route("/<string:name>")
def item_detail(name):
    item = Item.query.filter(Item.name == name).first()
    return render_template("item/detail.html", item=item)
