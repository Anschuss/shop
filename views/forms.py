from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from models import User


class RegForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    surname = StringField("surname", validators=[DataRequired()])
    phone_number = StringField("phone number",
                               validators=[DataRequired(), Length(min=11, max=11)])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("passwrod", validators=[DataRequired()])
    confirm_password = PasswordField("confirm password",
                                     validators=[EqualTo("password"), DataRequired()])

    submit = SubmitField("Sign up")

    def validate_email(self, email):
        user = User.query.filter(User.email == email).first()
        if user:
            raise ValidationError("That email is taken.Pleas Choose different one!")

    def validate_number(self, phone_number):
        user = User.query.filter(User.phone_number == phone_number).filter()
        if user:
            raise ValidationError("That number is taken.Pleas Choose different one!")


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = StringField("password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")
