from flask import Blueprint, render_template
from login_and_model import Item


general = Blueprint("general", __name__)


@general.route("/")
def general_page():
    items = Item.query.all()
    return render_template("general/general.html", items=items)
