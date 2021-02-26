from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import logout_user, login_user, login_required, current_user

from ...forms import *
from models import db, User, Order
from app import bcrypt

user = Blueprint("user", __name__)


@user.route("/reg", methods=["GET", "POST"])
def registration_page():
    form = RegForm()
    if request.method == "POST":
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(name=form.name.data, surname=form.surname.data,
                    email=form.email.data, phone_number=form.phone_number.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account is created")
        return redirect(url_for("user.login"))

    return render_template("user/reg.html", form=form)


@user.route("/log", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = User.query.filter(User.email == form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("general.general_page"))
        else:
            flash("Login Unsuccessful.Pleas check your email or password")

    return render_template("user/login.html", form=form)


@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@user.route("/account/<int:id>")
def detail_user(id):
    if current_user.id != id:
        return render_template("error/404.html")
    orders = Order.query.filter(Order.user_id == id).all()
    return render_template("user/detail.html", orders=orders)


@user.route("/order")
@login_required
def manager_page():
    if current_user.role_id != 2:
        return render_template("error/404.html")
    orders = Order.query.all()
    return render_template("user/manage.html", orders=orders)

