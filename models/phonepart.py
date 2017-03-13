from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from __init__ import db


class phonePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part = db.Column(db.Integer, db.ForeignKey('part.id'))
    phone = db.Column(db.Integer, db.ForeignKey('phone.id'))
 

    def __init__(self, partType, price):
        self.partName = partName
        self.price = price
        self.startDate = datetime.utcnow()
