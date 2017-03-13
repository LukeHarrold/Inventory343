from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from __init__ import db
import enum


class statusEnum(enum.Enum):
    NEW = "New"
    BROKEN = "Broken"
    REFURBISHED = "Refurbished"


class phone(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(statusEnum))
    model = db.Column(db.Integer, db.ForeignKey('phonetype.id'))
    saleDate = db.Column(db.DateTime)
    returnDate = db.Column(db.DateTime)
    refurbishedDate = db.Column(db.DateTime)

    
    def __init__(self, status, model):
        self.status = status
        self.model = model
