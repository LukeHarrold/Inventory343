from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import db
from flask import request



@app.route('/inventory/<num_parts>/<part_type_id>', methods=['GET'])
def send_part_information(num_parts, part_type_id):
	return


@app.route('/inventory/', methods=['POST'])
def receive_completed_phones():
	return