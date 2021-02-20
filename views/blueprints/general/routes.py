from flask import Blueprint, request, render_template, redirect, url_for
from models import Item


general = Blueprint("general", __name__)


@general.route("/")
def general_page():
    items = Item.query.all()
    return render_template("general/general.html", items=items)
