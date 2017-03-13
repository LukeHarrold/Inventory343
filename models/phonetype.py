from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from __init__ import db
import enum


class phoneEnum(enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    FLIP = "Flip"


class phoneType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phoneType = db.Column(db.Enum(phoneEnum))
    screenType = db.Column(db.Integer, db.ForeignKey('parttype.id'))
    batteryType = db.Column(db.Integer, db.ForeignKey('parttype.id'))
    memoryType = db.Column(db.Integer, db.ForeignKey('parttype.id'))
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
