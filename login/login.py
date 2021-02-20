from flask_login import LoginManager

login = LoginManager()
login.login_view = "login"
login.login_message_category = "info"