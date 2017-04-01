from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import request, jsonify, render_template, url_for, redirect
import requests
import random
import datetime
import re
from model import Part, Phone, PhoneType

import json
'''
status options:
1 = new
2 = broken
3 = refurbished

model options:
h = high
m = medium
l = low
r = retro

part model options:
1 = screen
2 = battery
3 = case
'''


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



@app.route('/inventory/phones/ordermock', methods=['POST'])
def phone_orders_mock():
	possibilities = [[200, True], [400, False]]
	whatHappened = random.choice(possibilities)
	return jsonify({'success':whatHappened[1]}), whatHappened[0]
   
''' 
Assuming this may be used once manufacturing has endpoints?
@app.route('/inventory/phones/order', methods=["POST"])
def create_new_phones(orderQuantity, phoneModelId):
	r = requests.post("http://127.0.0.1/manufacturing/order", orderQuantity, phoneModelId)
	return json.dumps({'success':True}), 200, {'ContentType' : 'application/json'}
'''

@app.route('/inventory/phones/order', methods=['GET', 'POST'])
def phone_orders():
	#None of this can be used, we have to wait for manufacturing and sales
	#data = request.get_json(force=True)
	#r = requests.post('http://127.0.0.1:5000/inventory/phones/ordermock', data = json.dumps(data))
	#print(r.status_code)
	return app.make_response((r.content, '200', {'Content-Type': 'application/json'}))

@app.route('/inventory/send/', methods=['GET'])
def send_broken_phones():
	'''
	Send phone to manufacturing to be refurbished.
	'''
	output = []
	phones_to_send = Phone.query.filter_by(status="Broken")
	for phone_to_send in phones_to_send:
		output.append(to_json_like_string(phone_to_send))
	print(output)
	return jsonify((output))
	
	#return json.dumps({'success':True}, 200, {'ContentType':'application/json'})


@app.route('/inventory/mock', methods=['POST'])
def stub_completed_phones():
	#Get phone information here
	num_phones = random.randint(1,10)
	phone_types = ['h', 'm', 'l', 'r']

	part_types = ['battery', 'screen', 'memory']
	#need to get battery, screen, and memory part number from db
	phones = []

	for phone in range(1, num_phones):
		battery = random.randint(1,1000)
		memory = random.randint(1001,10000)
		screen = random.randint(10001, 18000)
		

		phone_info = {}
		phone_info['id'] = phone
		phone_info['model'] = random.choice(phone_types)
		phone_info['battery'] = battery
		phone_info['memory'] = memory
		phone_info['screen'] = screen
		phones.append(phone_info)
	url = 'http://127.0.0.1:5000/inventory'
	r = requests.post(url, data=json.dumps(phones))
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/inventory/<data>/', methods=["POST"])
def receive_fixed_phones(data):
	'''
	Receives either new phones or refurbished phones from manufacturing with replaced parts
	'''
	print("getting called")
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
		output.append(to_json_like_string(model))
	return jsonify(output)

@app.route('/inventory/models/<phoneModelId>', methods=['GET'])
def holding_sales_hand_through_indexing(phoneModelId):
	'''
	Returns a specific type of phone
	'''
	phoneModel = PhoneType.query.filter( PhoneType.id==phoneModelId ).first()
	output = to_json_like_string(phoneModel)
	return jsonify(output)

@app.route('/inventory/phone/return/<phoneId>', methods=['GET'])	
def mark_as_returned(phoneId):
	'''
	Marks a specific phone as “returned”
	'''
	returned_phone = Phone.query.filter(Phone.id==phoneId).first()
	returned_phone.returnDate = datetime.datetime.now()
	db.session.commit()
	return json.dumps(({'success':True}, 200, {'ContentType' : 'application/json'}))

@app.route('/inventory/phones/<phoneId>', methods=['GET'])	
def get_phone_by_id(phoneId):
	'''
	Returns a specific phone based on its uid, or serial number
	'''

	phone_to_send = Phone.query.filter(Phone.id==phoneId).first()
	output = to_json_like_string(phone_to_send)
	return jsonify((output))

	phone_models = ['h', 'm', 'l', 'f']
	statuses = ['New', 'Broken', 'Refurbished']
	phone = {}
	phone['id'] = phoneId
	phone['model'] = random.choice(phone_models)
	phone['status'] =  random.choice(statuses)
	phone['screen'] = random.randint(1,1000)
	phone['memory'] = random.randint(1,1000)
	phone['keyboard'] = random.randint(1,1000)
	return json.dumps(phone)

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

