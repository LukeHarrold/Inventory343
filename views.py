from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import request, jsonify, render_template, url_for, redirect
import requests
import random

import json


@app.route('/inventory/<num_parts>/<part_type_id>', methods=['GET'])
def send_part_information(num_parts, part_type_id):
	return


@app.route('/')
def hello():
    return render_template('layout.html')

@app.route('/inventory/', methods=['GET', 'POST'])
def stub_completed_phones():
	#Get phone information here
	num_phones = random.randint(1,4)
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
	url = 'http://localhost:5000/inventory/us'
	p = json.dumps(phones)
	r = requests.post(url, data=p)
	return r


@app.route('/inventory/us/', methods=['POST', 'GET'])
def receive_completed_phones():
	print('bb we rolling')
	print(request.method)
	if request.method == 'POST':
		print("is a post*******************")
		phones = request.get_json()
		print(phones)
		#phone_info = json.load(phones)
	#	print(phone_info)
#		return redirect(url_for('/'))
	else:
		print("why")
	return redirect(url_for('hello'))

@app.route('/inventory/phones/ordermock', methods=['POST'])
def phone_orders():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

