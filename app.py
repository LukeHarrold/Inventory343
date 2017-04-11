from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import render_template
import csv


db.create_all()
import model

@app.route("/")
def hello():
	dummyphones = open('DummyData/dummyphonetable.csv')
	dummyparts = open('DummyData/dummypartstable.csv')
	dummyavailable = open('DummyData/dummyavailablephones.csv')

	return render_template('layout.html', table1data = csv.reader(dummyphones), table2data = csv.reader(dummyparts), table3data = csv.reader(dummyavailable))


if __name__ == "__main__":
    app.run(threaded=True)


 

