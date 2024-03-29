from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

# creating an instance of a Flask app
app = Flask(__name__)

# bring our configuration
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


from . import routes, models