from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True #removes annoying message
path = 'sqlite:///' + os.path.dirname(os.path.abspath(__file__)) + '/swen-343-inventory.db'
app.config['SQLALCHEMY_DATABASE_URI'] = path
db = SQLAlchemy(app)

# import the models *after* the db object is define

from models import parttype
from models import phonetype
from models import phone
from models import part
from models import phonepart
import views
