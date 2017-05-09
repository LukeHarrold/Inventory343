from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from __init__ import app, db
from flask import request, jsonify, render_template, url_for, redirect
import requests
import random
import datetime
import re
from model import Part, Phone, PhoneType, PartType
import csv

import json

@app.route("/")
def landing():
	all_inventory_phones = {}
	parts = {}

	#grab all phone models
	all_models = PhoneType.query.all()
	#build dictionary entry for model
	for model in all_models:
		if model.id not in all_inventory_phones:
			all_inventory_phones[model.id] = {"New": [], "Refurbished": [], "Broken": []}

	#grab all phones
	all_phones = Phone.query.all()
	
	#check if phone is in inventory and add it into proper place
	for phone in all_phones: 
		if in_inventory(phone):
			if phone.status in all_inventory_phones[phone.modelId]:
				all_inventory_phones[phone.modelId][phone.status].append(phone)
			else:
				all_inventory_phones[phone.modelId][phone.status] = [phone]

	#grab available parts
	all_parts = Part.query.filter_by(used=0).filter_by(defective=0).all()

	for part in all_parts:
		if part.partTypeId in parts:
			parts[part.partTypeId].append(part)
		else:
			parts[part.partTypeId] = [part]

	part_names = {}
	part_types = PartType.query.all()
	for part in part_types:
		cap_loc = re.search('[A-Z][^A-Z]*', part.partName)
		if cap_loc:
			final_name = ''
			span = cap_loc.span()
			final_name = (part.partName[:span[0]] + ' ' + part.partName[span[0]:]).title()
		else:
			final_name = part.partName.title()
		part_names[part.id] = final_name

	return render_template('layout.html', all_inventory_phones = all_inventory_phones, all_models = all_models, parts=parts, part_names=part_names)

def in_inventory(phone):
	if phone.saleDate == None:
		return True
	else:
		if phone.returnDate == None:
			return False
		elif phone.saleDate > phone.returnDate:
			return True
		else:
			return False

@app.route('/inventory/parts/purchase', methods=['GET'])		
def purchase_parts_form():
	part_types = PartType.query.all()
	return render_template('purchase.html', part_types=part_types)

@app.route('/inventory/parts/accounting', methods=['GET', 'POST'])		
def purchase_parts_accounting():
	result = request.form
	part_request_name = result['part_type']
	part_request_amount = result['part_amount']
	part_info = PartType.query.filter_by(partName=part_request_name).first()
	part_price = part_info.price
	total_price = float(part_price)*round(float(part_request_amount))

	purchase_dict = {"amount": total_price}
	jsonify(purchase_dict)
	requests.post('http://vm343e.se.rit.edu/inventory', json=purchase_dict)
	model_info = None

	model_info = PhoneType.query.filter_by(screenTypeId=part_info.id).first()
	if not model_info:
		model_info = PhoneType.query.filter_by(batteryTypeId=part_info.id).first()
		if not model_info:
			model_info = PhoneType.query.filter_by(memoryTypeId=part_info.id).first()
	num_created = 0
	partType = part_info.id
	modelType = model_info.id

	request_amount = round(float(part_request_amount))
	while num_created < request_amount:
		part = Part(partType, modelType)
		db.session.add(part)
		num_created += 1
	db.session.commit()
	return redirect(url_for('landing'))


@app.route('/inventory/phone/recall/<model_id>')
def mark_as_recalled(model_id):
	#Mark model as recalled

	try:
		specific_model = PhoneType.query.filter_by( id=model_id )
	except:
		return 

	specific_model.isRecalled = True

	#mark status of phone as recalled
	get_phone_type = PhoneType.query.filter_by(id = model_id)
	for phone_type in get_phone_type:
		phone_type.isRecalled = True
	get_phones = Phone.query.filter_by(modelId=model_id)
	for phone in get_phones:
		phone.status = "Recalled"
		get_parts = Part.query.filter_by(phoneId=phone.id)
		# Mark all the parts for each phone as recalled.
		for part in get_parts:
			part.isRecalled = True


	db.session.commit()
	return app.make_response(('200', {'Content-Type': 'application/json'}))


@app.route('/inventory/get-parts/<num_parts>/<part_type_id>', methods=['GET'])
def send_part_information(num_parts, part_type_id):
	'''
	Sends the part information for the number and type of part specified.
	'''
	sent=0
	output = []
	parts_to_send = Part.query.filter_by( partTypeId=part_type_id).filter_by(phoneId =None ).all()
	for part_to_send in parts_to_send:
		if part_to_send.phoneId == None:
			output.append( to_json_like_string(part_to_send))
			sent += 1
			if sent >= int(num_parts):
				break
	return jsonify(output)

@app.route('/inventory/phones/order', methods=['GET', 'POST'])
def phone_orders():
	return app.make_response((r.content, '200', {'Content-Type': 'application/json'}))

@app.route('/inventory/send/', methods=['GET'])
def send_broken_phones():
	'''
	Send phone to manufacturing to be refurbished.
	'''
	output = []
	phones_to_send = Phone.query.filter_by(status="Broken")
	for phone_to_send in phones_to_send:
		output.append(to_json_like_string(phone_to_send)[0]["fields"])
	return jsonify((output))

@app.route('/inventory/', methods=["POST"])
def receive_phones():
	'''
	Receives either new phones or refurbished phones from manufacturing with replaced parts
	'''
	phones = request.get_json()
	phone_type = ''

	if phones["phones"][0]["status"].lower() == 'new':
		phone_type = 'new'
	elif phones["phones"][0]["status"].lower() == 'refurbished':
		phone_type = 'refurbished'

	if phone_type == 'new':
		for phone in phones["phones"]:
			modelId = phone["modelID"]
			status = phone["status"]
			phone_to_add = Phone(status, modelId)
			db.session.add(phone_to_add)

			screen, battery, memory = phone["partIDs"]

			db_screen = Part.query.filter_by(id=screen).first()
			db_screen.phoneId = phone_to_add.id
			db_screen.used = True

			db_battery = Part.query.filter_by(id=battery).first()
			db_battery.phoneId = phone_to_add.id
			db_battery.used=True

			db_memory = Part.query.filter_by(id=memory).first()
			db_memory.phoneId = phone_to_add.id
			db_memory.used=True

			db.session.commit()
	elif phone_type == 'refurbished':
		for phone in phones["phones"]:
			phoneId = phone["phoneID"]
			db_phone = Phone.query.filter_by(id=phoneId).first()
			db_phone.status = "Refurbished"
			db_phone.refurbishedDate = datetime.datetime.now()

			screen, battery, memory = phone["partIDs"]
			broken = phone["broken"]

			db_broken = Part.query.filter_by(id=broken).first()
			db_broken.defective=True
			db_broken.phoneId = None
			db_broken.used=False

			db_screen = Part.query.filter_by(id=screen).first()
			db_screen.phoneId = phoneId
			db_screen.used=True

			db_battery = Part.query.filter_by(id=battery).first()
			db_battery.phoneId = phoneId
			db_battery.used=True

			db_memory = Part.query.filter_by(id=memory).first()
			db_memory.phoneId = phoneId
			db_memory.used=True
			db.session.commit()


	return app.make_response(('200', {'Content-Type': 'application/json'}))


@app.route('/inventory/models/all', methods=["GET"])
def all_phone_models():
	'''
	Returns a list of all the models in the inventory
	'''
	all_models = PhoneType.query.all()
	output = []
	for model in all_models:
		output.append(to_json_like_string(model)[0]["fields"])
	return jsonify(output)

@app.route('/inventory/models/<phoneModelId>', methods=['GET'])
def return_specific_model(phoneModelId):
	'''
	Returns a specific type of phone
	'''
	phoneModel = PhoneType.query.filter( PhoneType.id==phoneModelId ).first()
	output = jsonify(to_json_like_string(phoneModel)[0]["fields"])
	return (output)

@app.route('/inventory/phone/return/<phoneId>', methods=['GET'])	
def mark_as_returned(phoneId):
	returned_phone = Phone.query.filter(Phone.id==phoneId).first()
	returned_phone.returnDate = datetime.datetime.now()
	db.session.commit()
	
	modelId = returned_phone.modelID

	#from model id, get part ids
	model_information = PhoneType.query.filter_by(id=modelId).first()
	#ask for each part id individually
	screen = Part.query.filter(Part.modelType==modelID and Part.phoneId==returned_phone.id and Part.partTypeId==model_information.screenTypeId).first()
	battery = Part.query.filter(Part.modelType==modelID and Part.phoneId==returned_phone.id and Part.partTypeId==model_information.batteryTypeId).first()
	memory = Part.query.filter(Part.modelType==modelID and Part.phoneId==returned_phone.id and Part.partTypeId==model_information.memoryTypeId).first()


	return json.dumps(({'success':True}, 200, {'ContentType' : 'application/json'}))

@app.route('/inventory/phone/order/<modelId>/<numPhones>', methods=['GET'])
def get_phones(modelId, numPhones):
	phones = Phone.query.filter(Phone.modelId==modelId).limit(numPhones).all()
	output=[]
	for phone in phones:
		output.append(to_json_like_string(phone)[0]["fields"])
		
	return jsonify(output)

@app.route('/inventory/phone/mark_bogo/<phoneId>', methods=['GET'])
def mark_as_bogo(phoneId):
	bogo_phogo = Phone.query.filter(Phone.id == phoneId).first()
	bogo_phogo.bogo = True
	db.session.commit()
	return jsonify(to_json_like_string(bogo_phogo)[0]["fields"])

@app.route('/inventory/phones/<phoneId>', methods=['GET'])	
def get_phone_by_id(phoneId):
	'''
	Returns a specific phone based on its uid, or serial number
	'''
	phone_to_send = Phone.query.filter(Phone.id==phoneId).first()
	output = to_json_like_string(phone_to_send)[0]["fields"]
	return jsonify((output))


def to_json_like_string(model_in):
	""" Returns a JSON representation of an SQLAlchemy-backed object
	"""
	json_in = {}
	json_in['fields'] = {}
	json_in['pk'] = getattr(model_in, 'id')

	for col in model_in._sa_class_manager.mapper.mapped_table.columns:
		if isinstance(getattr(model_in, col.name), datetime.datetime):
			json_in['fields'][col.name] = getattr(model_in, col.name).strftime("%m/%d/%Y")
		else:
			json_in['fields'][col.name] = getattr(model_in, col.name)

	return ([json_in])

