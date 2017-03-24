from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import request
from flask import render_template

import json



@app.route('/inventory/<num_parts>/<part_type_id>', methods=['GET'])
def send_part_information(num_parts, part_type_id):
	return


@app.route("/")
def hello():
    return render_template('layout.html')


@app.route('/inventory/', methods=['POST'])
def receive_completed_phones():
	return


@app.route('/inventory/phones/ordermock', methods=['POST'])
def phone_orders():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

