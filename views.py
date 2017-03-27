from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import request, jsonify, render_template, url_for, redirect
import requests
import random
import datetime
from models import *

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
f = flip phone

part model options:
1 = screen
2 = battery
3 = case
'''

@app.route('/')
def hello():
    return render_template('layout.html')

@app.route('/inventory/get-parts/<num_parts>/<part_type_id>', methods=['GET'])
def send_part_information(num_parts, part_type_id):
	phone_models = ["h", "l", "m", "f"]
	part_types = ["battery", "screen", "memory"]
	parts = []
	url = "http://127.0.0.1:5000/inventory/{}/{}".format(num_parts, part_type_id)
	for part in range(int(num_parts)):
		part_row = {}
		part_row["id"] = random.randint(1,1000) 
		part_row["model"] = random.choice(phone_models)
		part_row["part_type"] = part_type_id
		part_row["defective"] = False
		part_row["part_type"] = random.choice(part_types)
		parts.append(part_row)
	print(json.dumps(parts))
	#r = requests.get(url, data=json.dumps(parts))
	return json.dumps(parts)


@app.route('/inventory/mock', methods=['GET', 'POST'])
def stub_completed_phones():
	#Get phone information here
	num_phones = random.randint(1,10)
	phone_types = ['h', 'm', 'l', 'f']

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
	print('original')
	print(json.dumps(phones))
	r = requests.post(url, data=json.dumps(phones))
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/inventory', methods=['POST'])
def receive_completed_phones():

	phones = request.get_json(force=True)
	print('received')
	print(phones)

	date = datetime.now()
	status = 1


	#assosciate with part data

	#Get description/price/img path from db based on model

	#phone_info = json.load(phones)
#	print(phone_info)
#		return redirect(url_for('/'))
	return app.make_response("200")

@app.route('/inventory/phones/ordermock', methods=['POST'])
def phone_orders_mock():
    possibilities = [[200, True], [400, False]]
    whatHappened = random.choice(possibilities)
    return json.dumps({'success':whatHappened[1]}), whatHappened[0]
    


@app.route('/inventory/phones/order', methods=['POST'])
def phone_orders():
    data = request.get_json(force=True)
    r = requests.post('http://127.0.0.1:5000/inventory/phones/ordermock', data = json.dumps(data))
    print(r.status_code)
    return app.make_response((r.content, r.status_code, {'Content-Type': 'application/json'}))

@app.route('/inventory/send', methods=['POST'])
def send_broken_phones(phoneRow):
	phone_models = ['h', 'm', 'l', 'f']
	phone={}
	phone["id"] = random.randint(1,1000)
	phone["model"] = random.choice(phone_models)
	phone["status"] = "Broken"
	phone["screen"] = random.randint(1,1000)
	phone["memory"] = random.randint(1,1000)
	phone["keyboard"] = random.randint(1,1000)
	r = requests.post("http://127.0.0.1/inventory", data=json.dumps(phone))
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/inventory', methods=['POST'])
def receive_fixed_phones(phoneRow):
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

@app.route('/inventory/phones/order', methods=['POST'])
def create_new_phones(orderQuantity, phoneModelId):
	r = requests.post("http://127.0.0.1/manufacturing/order", orderQuantity, phoneModelId)
	return json.dumps({'success':True}), 200, {'ContentType' : 'application/json'}

@app.route('/inventory/models/all', methods=["GET"])
def all_phone_models():
	phone_models = ['h', 'm', 'l', 'f']
	all_models = []
	for model in phone_models:
		all_models.append({"id":phone_models.index(model), "model":model, "description":model, "price":25*phone_models.index(model)})

	return json.dumps(all_models)

@app.route('/inventory/models/<phoneModelId>', methods=['GET'])
def holding_sales_hand_through_indexing(phoneModelId):
	phone_models = ['h', 'm', 'l', 'f']
	return json.dumps({"id": phoneModelId, "model" : phone_models[int(phoneModelId)%4], "description": phone_models[int(phoneModelId)%4], "price":25*int(phoneModelId),
		"memory" : random.randint(1,1000),
		"screen" : random.randint(1,1000),
		"keyboard" : random.randint(1,1000)})


@app.route('/inventory/phone/return?phoneid=<phoneId>', methods=['GET'])	
def mark_as_returned(phoneId):

	return json.dumps({'success':True}, 200, {'ContentType' : 'application/json'})

@app.route('/inventory/phones/<phoneId>', methods=['GET'])	
def get_phone_by_id(phoneId):
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

