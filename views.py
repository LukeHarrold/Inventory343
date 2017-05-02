from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
	part_names = {}
	part_types = PartType.query.all()

	return render_template('purchase.html', part_types=part_types)

@app.route('/inventory/parts/accounting', methods=['GET', 'POST'])		
def purchase_parts_accounting():
	result = request.form
	part_request_name = result['part_type']
	part_request_amount = result['part_amount']
	part_info = PartType.query.filter_by(partName=part_request_name).first()
	part_price = part_info.price
	total_price = float(part_price)*float(part_request_amount)

	purchase_dict = {"amount": total_price}
	jsonify(purchase_dict)
	requests.post('http://vm343e.se.rit.edu/inventory', json=purchase_dict)

	"""
	#for part in part_request_amount:
		#get part type id
		#Get model
		#defective=False
		#used=False
		#phoneId
		#bogo=False
		self.partTypeId = partType
        self.modelType = modelType
        self.defective = False
        self.used = False
        phoneId = phoneId
        bogo = False
    """
	return redirect(url_for('landing'))


@app.route('/inventory/phone/recall/<model_id>')
def mark_as_recalled(model_id):

	return app.make_response(('200', {'Content-Type': 'application/json'}))


@app.route('/inventory/get-parts/<num_parts>/<part_type_id>', methods=['GET'])
def send_part_information(num_parts, part_type_id):
	'''
	Sends the part information for the number and type of part specified.
	'''
	output = []
	parts_to_send = Part.query.filter_by( partTypeId=part_type_id and Part.phoneId == None ).all()
	for part_to_send in parts_to_send:
		output.append( to_json_like_string(part_to_send))
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
	

@app.route('/inventory/<data>/', methods=["POST"])
def receive_fixed_phones(data):
	'''
	Receives either new phones or refurbished phones from manufacturing with replaced parts
	'''
	num_phones = random.randint(1,10)
	phone_models = ['h', 'm', 'l', 'f']
	phones=[]
	for phone in range(num_phones):
		phone_row = {}
		phone_row["id"] = random.randint(1,100)
		phone_row["model"] = random.choice(phone_models)
		phone_row["status"] = "Refurbished"
		phone_row["screen"] = random.randint(1,1000)
		phone_row["memory"] = random.randint(1,1000)
		phone_row["keyboard"] = random.randint(1,1000)
		phones.append(phone_row)
	r = requests.post("http://127.0.0.1/inventory", data=json.dumps(phones))
	return json.dumps({'success':True}), 200, {'ContentType' : "application/json"}


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
	return json.dumps(({'success':True}, 200, {'ContentType' : 'application/json'}))

@app.route('/inventory/phone/order/<modelId>/<numPhones>', methods=['GET'])
def get_phones(modelId, numPhones):
	phones = Phone.query.filter(Phone.modelId==modelId).limit(numPhones).all()
	output = to_json_like_string(phones)[0]["fields"]
	return jsonify(output)

@app.route('/inventory/phone/mark_bogo/<phoneId>', methods=['GET'])
def mark_as_bogo(phoneId):
	bogo_phogo = Phone.query.filter(Phone.Id == phoneId).first()
	bogo_phogo.Bogo = 1
	db.session.commit()
	return jsonify((bogo_phogo))

@app.route('/inventory/phones/<phoneId>', methods=['GET'])	
def get_phone_by_id(phoneId):
	'''
	Returns a specific phone based on its uid, or serial number
	'''

	phone_to_send = Phone.query.filter(Phone.id==phoneId).first()
	output = to_json_like_string(phone_to_send)
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

