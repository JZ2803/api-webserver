from os import environ
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Define the Flask application
app = Flask(__name__)

# Set the secret key for JWT authentication
app.config['JWT_SECRET_KEY'] = environ.get('SECRET_KEY')

# Set the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

# Set the Flask-Marshmallow configuration to sort keys in alphabetical order to false
app.json.sort_keys = False

# Initialize SQLAlchemy with the specified database URI
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Initialize Flask-Marshmallow with the Flask application
ma = Marshmallow(app)

# Initialize Flask-Bcrypt with the Flask application
bcrypt = Bcrypt(app)

# Initialize Flask-JWT-Extended with the Flask application
jwt = JWTManager(app)