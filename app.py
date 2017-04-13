from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import render_template
import csv


db.create_all()
import model


if __name__ == "__main__":
    app.run(threaded=True)


 

