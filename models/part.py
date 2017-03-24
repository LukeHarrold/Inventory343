from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import db


class Part(db.Model):
    __tablename__ = 'parts'
    id = db.Column(db.Integer, primary_key=True)
    parttype_id = db.Column(db.Integer, db.ForeignKey('part_types.id'))#We may want to change the primary key to use 2 strings such as battery, low
    price = db.Column(db.Float)
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    deletedAt = db.Column(db.DateTime)

 

    def __init__(self, partType, price):
        self.partType = partType
        self.price = price
        self.startDate = datetime.utcnow()
