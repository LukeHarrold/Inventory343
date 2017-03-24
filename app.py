from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app, db
import configparser
from flask import render_template

config = configparser.ConfigParser()
configValues = config.read("config.ini")
if len(configValues) < 1:
    # Will add aditional items to the config file as neeeded.
    config['swen-343-database'] = {}
    config['swen-343-database']['uri'] = input('Enter the DB URI: ')
    # config['swen-343-server'] = {}
    # config['swen-343-server']['admin'] = {}
    # config['swen-343-server']['admin']['username'] = input('Enter the desired server admin username:')
    # config['swen-343-server']['admin']['password'] = input('Enter the desired server admin password:')
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['swen-343-database']['uri']
# db = SQLAlchemy(app)


@app.route("/")
def hello():
    return render_template('layout.html')


if __name__ == "__main__":
    app.run()