from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
from flask import render_template


if __name__ == "__main__":
    app.run()