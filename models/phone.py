from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from __init__ import db


class Phone(db.Model):
    __tablename__ = 'phones'
    id  = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    model_id = db.Column(db.Integer, db.ForeignKey('phone_types.id'))
    saleDate = db.Column(db.DateTime)
    returnDate = db.Column(db.DateTime)
    refurbishedDate = db.Column(db.DateTime)

    
    def __init__(self, status, model):
        self.status = status
        self.model = model
