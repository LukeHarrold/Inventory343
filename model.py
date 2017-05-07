from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from __init__ import db

class Part(db.Model):
    __tablename__ = 'parts'
    id = db.Column(db.Integer, primary_key=True)
    modelType = db.Column(db.Integer, db.ForeignKey('phone_types.id'))
    defective = db.Column(db.Boolean)
    used = db.Column(db.Boolean)
    partTypeId = db.Column(db.Integer, db.ForeignKey('part_types.id'))#We may want to change the primary key to use 2 strings such as battery, low
    phoneId = db.Column(db.Integer, db.ForeignKey('phones.id'))
    bogo = db.Column(db.Boolean)
    isRecalled = db.Column(db.Boolean)


    def __init__(self, partType, modelType):
        self.partTypeId = partType
        self.modelType = modelType
        self.defective = False
        self.used = False
        self.phoneId = None
        self.bogo = False
        self.isRecalled = False


### EXPERIMENTAL ###
# to restore to previous schema, remove line 13 and comment in lines 39 and 40
#phoneParts = db.Table('phone_parts',
#    db.Column('phone_id', db.Integer, db.ForeignKey('phones.id')),
#    db.Column('part_id', db.Integer, db.ForeignKey('parts.id'))
#)


class Phone(db.Model):
    __tablename__ = 'phones'
    id  = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80))
    modelId = db.Column(db.Integer, db.ForeignKey('phone_types.id'))
    saleDate = db.Column(db.DateTime)
    returnDate = db.Column(db.DateTime)
    refurbishedDate = db.Column(db.DateTime)
    bogo = db.Column(db.Boolean)

    #parts = db.relationship('Part', secondary=phoneParts,
    #    backref=db.backref('parts', lazy='dynamic'))

    
    def __init__(self, status, model):
        self.status = status
        self.modelId = model
        self.saleDate = None
        self.returnDate = None
        self.refurbishedDate = None
        self.bogo = False


class PhoneType(db.Model):
    __tablename__ = 'phone_types'
    id = db.Column(db.Integer, primary_key=True)
    phoneType = db.Column(db.String(80))
    screenTypeId = db.Column(db.Integer, db.ForeignKey('part_types.id'))
    batteryTypeId = db.Column(db.Integer, db.ForeignKey('part_types.id'))
    memoryTypeId = db.Column(db.Integer, db.ForeignKey('part_types.id'))
    description = db.Column(db.String(300))
    imagePath = db.Column(db.String(300))
    price = db.Column(db.Float)
    deletedAt = db.Column(db.DateTime)
    phones = db.relationship('Phone', backref='phone_types', lazy='dynamic')
    isRecalled = db.Column(db.Boolean)

    # screenType = db.relationship('PartType', foreign_keys = 'screenTypeId')
    # batteryType = db.relationship('PartType', foreign_keys = 'batteryTypeId')
    # memoryType = db.relationship('PartType', foreign_keys = 'memoryTypeId')


    def __init__(self, phoneType, screenType, batteryType, memoryType, description, imagePath, price):
        self.phoneType = phoneType
        self.screenTypeId = screenType
        self.batteryTypeId = batteryType
        self.memoryTypeId = memoryType
        self.description = description
        self.imagePath = imagePath
        self.price = price
        self.deletedAt = None
        self.isRecalled = False


class PartType(db.Model):
    __tablename__ = 'part_types'
    id = db.Column(db.Integer, primary_key=True)
    partName = db.Column(db.String(80))#We may want to change the primary key to use 2 strings such as battery, low
    price = db.Column(db.Float)
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    deletedAt = db.Column(db.DateTime)
    parts = db.relationship('Part', backref='part_type', lazy='dynamic')
    
    # phoneTypes = db.relationship('PhoneType', backref='part_types', lazy='dynamic')
    batteryPart = db.relationship('PhoneType', backref='battery', lazy='dynamic', foreign_keys='[PhoneType.batteryTypeId]')
    screenPart = db.relationship('PhoneType', backref='screen', lazy='dynamic', foreign_keys='[PhoneType.screenTypeId]')
    memoryPart = db.relationship('PhoneType', backref='memory', lazy='dynamic', foreign_keys='[PhoneType.memoryTypeId]')


    def __init__(self, partName, price):
        self.partName = partName
        self.price = price
        self.startDate = datetime.utcnow()
        self.endDate = None
        self.deletedAt = None

