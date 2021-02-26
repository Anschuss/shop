from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from config import Configuration, make_celery

app = Flask(__name__)
app.config.from_object(Configuration)

### CELERY ###

client = make_celery(app)
client.conf.update(app.config)

### DB ###
from login_and_model import db, Order, Item

db.init_app(app)
migrate = Migrate(app, db)

### Login ###

bcrypt = Bcrypt(app)
from login_and_model import login

login.init_app(app)

### Blueprints ###

from views import *

app.register_blueprint(user, url_prefix="/")
app.register_blueprint(general, url_prefix="/")
app.register_blueprint(item, url_prefix="/item")

### Admin ###

admin = Admin(app)
admin.add_view(ModelView(User, db.session, endpoint="users_"))
admin.add_view(ModelView(Item, db.session, endpoint="item_"))
admin.add_view(ModelView(Order, db.session, endpoint="order_"))


