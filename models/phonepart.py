from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from __init__ import db


class PhonePart(db.Model):
    __tablename__ = 'phone_parts'
    id = db.Column(db.Integer, primary_key=True)
    part_id = db.Column(db.Integer, db.ForeignKey('parts.id'))
    phone_id = db.Column(db.Integer, db.ForeignKey('phones.id'))
 

    def __init__(self, partType, price):
        self.partName = partName
        self.price = price
        self.startDate = datetime.utcnow()
