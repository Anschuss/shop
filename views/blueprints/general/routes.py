from flask import Blueprint, request, render_template, redirect, url_for

general = Blueprint("general", __name__)


@general.route("/")
def general_page():
    return render_template("general/general.html")
