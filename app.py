from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import render_template
import csv

import model
db.create_all()


if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, port=5000)


 

