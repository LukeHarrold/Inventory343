from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import request, jsonify, render_template
import random



app = Flask(__name__)

@app.route('/inventory/<num_parts>/<part_type_id>', methods=['GET'])
def send_part_information(num_parts, part_type_id):
	return


@app.route('/')
def hello():
    return render_template('layout.html')


def stub_completed_phones():
	#Get phone information here
	num_phones = random.randint(1,300)
	phone_types = ['h', 'm', 'l', 'f']

	battery = random.randint(1,1000)
	memory = random.randint(1001,10000)
	screen = randint(10001, 18000)

	part_types = ['battery', 'screen', 'memory']
	#need to get battery, screen, and memory part number from db
	phones = []


	for phone in num_phones:
		phone_info = {}
		phone_info['model'] = random.choice(phone_types)
		phone_info['battery'] = battery
		phone_info['memory'] = memory
		phone_info['screen'] = screen
		phones.append(phone_info)
	return jsonify(phones)


@app.route('/inventory/')
def receive_completed_phones():
	print('here')
	phones = stub_completed_phones()
	phone_info = json.loads(phones)
	print(phone_info)
	return redirect(url_for('/'))
