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
	print(num_parts, part_type_id)
	parts = part.Part.query.all()


	return render_template('basic_display.html', data=parts)

@app.route('/inventory/get-parts/mock', methods=['GET'])
def stub_part_information():
	num_parts = random.randint(1, 30)
	part_type_id = random.randint(1, 3)

	temp = url_for('send_part_information', num_parts=num_parts, part_type_id=part_type_id)
	url = 'http://127.0.0.1:5000' + str(temp)
	r = requests.get(url)
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

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

	return app.make_response("200")

@app.route('/inventory/phones/ordermock', methods=['POST'])
def phone_orders_mock():
    orderData = request.get_json(force=True)
    print(orderData)
    r = requests.post('http://127.0.0.1:5000/inventory/phones/order', data = json.dumps({"key": "test data"}))
    print(r)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/inventory/phones/order', methods=['POST'])
def phone_orders():
    print("HEYYYYYOOOOOO")
    data = request.get_json(force=True)
    print(data)

    return app.make_response("junk")


