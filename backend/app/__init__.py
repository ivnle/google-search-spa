from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
login = LoginManager(app)
login.login_view = 'login'

from . import routes, models
