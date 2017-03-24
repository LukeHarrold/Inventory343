from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from __init__ import db


class PhoneType(db.Model):
    __tablename__ = 'phone_types'
    id = db.Column(db.Integer, primary_key=True)
    phoneType = db.Column(db.Integer)
    screenType = db.Column(db.Integer, db.ForeignKey('part_types.id'))
    batteryType = db.Column(db.Integer, db.ForeignKey('part_types.id'))
    memoryType = db.Column(db.Integer, db.ForeignKey('part_types.id'))
    description = db.Column(db.String(300))
    imagePath = db.Column(db.String(300))
    price = db.Column(db.Float)
    deletedAt = db.Column(db.DateTime)
    

    def __init__(self, phoneType, screenType, batteryType, memoryType, description, imagePath, price):
        self.phoneType = phoneType
        self.screenType = screenType
        self.batteryType = batteryType
        self.memoryType = memoryType
        self.description = description
        self.imagePath = imagePath
        self.price = price
        self.saleDate = datetime.utcnow()
