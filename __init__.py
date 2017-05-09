from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import ConfigParser

config = ConfigParser.ConfigParser()

try:
    config.read("config.ini")
except:
    config = None


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True #removes annoying message
if config != None:
    path = 'mysql://' + config.get('MYSQLINFO','username') + ':' + config.get('MYSQLINFO', 'password') + '@localhost/inventory'
else:
    path = 'mysql://root:shiesh7aiN@localhost/inventory'

app.config['SQLALCHEMY_DATABASE_URI'] = path
db = SQLAlchemy(app)

# import the models *after* the db object is define

# from models import parttype
# from models import phonetype
# from models import phone
# from models import part
# from models import phonepart
from model import *
import views
