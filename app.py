from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import render_template
import csv

import model
db.create_all()


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host='0.0.0.0', threaded=True, port=8080)
=======
    app.run(host='0.0.0.0', threaded=True, port=80)
>>>>>>> 74969fb3cfac72683170e71d3d18fbff27cc69e7


 

