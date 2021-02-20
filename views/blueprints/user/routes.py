from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import current_user, logout_user, login_required, login_user

from ...forms import *
from models import db, User
from app import bcrypt

user = Blueprint("user", __name__)


@user.route("/reg", methods=["GET", "POST"])
def registration_page():
    form = RegForm()
    if request.method == "POST":
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(name=form.name.data, surname=form.surname.data,
                    email=form.email.data, phone_number=form.phone_number.data,
                    password=hashed_password, item=None)
        db.session.add(user)
        db.session.commit()
        flash("Your account is created")
        return redirect(url_for("login_user"))

    return render_template("user/reg.html", form=form)


@user.route("/log", methods=["GET", "POST"])
def login_user():
    form = LoginForm()
    if request.method == "POST":
        user = User.query.filter(User.email == form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for(""))
        else:
            flash("Login Unsuccessful.Pleas check your email or password")

    return render_template("user/login.html", form=form)
