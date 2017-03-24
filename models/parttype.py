from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from __init__ import db



class PartType(db.Model):
    __tablename__ = 'part_types'
    id = db.Column(db.Integer, primary_key=True)
    partName = db.Column(db.String(80))#We may want to change the primary key to use 2 strings such as battery, low
    price = db.Column(db.Float)
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    deletedAt = db.Column(db.DateTime)

 

    def __init__(self, partName, price):
        self.partName = partName
        self.price = price
        self.startDate = datetime.utcnow()
