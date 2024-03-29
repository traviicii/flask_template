from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

# creating an instance of a Flask app
app = Flask(__name__)

# bring our environment configurations
app.config.from_object(Config)

# create an instance of SQLAlchemy for our app to use
db = SQLAlchemy(app)

# create an instance of flask_migrate for our app to utilize
migrate = Migrate(app, db)


# let our app know about any files it needs to know about
from . import routes, models