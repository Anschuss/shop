from flask import Flask
from flask_migrate import Migrate

from flask_bcrypt import Bcrypt

from config import Configuration
from models import db

app = Flask(__name__)
app.config.from_object(Configuration)

### DB ###

db.init_app(app)
migrate = Migrate(app, db)

### Login ###

bcrypt = Bcrypt(app)
from login import login

login.init_app(app)

### Blueprints ###

from views import *

app.register_blueprint(user, url_prefix="/")
app.register_blueprint(general, url_prefix="/")