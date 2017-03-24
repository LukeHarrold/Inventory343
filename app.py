from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import render_template


db.create_all()
print("running")



if __name__ == "__main__":
    app.run(threaded=True)

