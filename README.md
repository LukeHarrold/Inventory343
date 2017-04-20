# Setting up the Project:
Make sure you have python 3 installed
Install the required packages using pip (pip3 if python 2 is your default):
```
pip install flask
pip install flask-sqlalchemy
pip install requests
```
# Setting up the database:
Our database is running on sqlite3.  Open the database file in the folder of the project (path_to_project/Inventory343/swen-343-inventory.db) and read in the setup.sql file.
```
sqlite3 swen-343-inventory.db
.read setup.sql
```

# Running the project:
In the Inventory343 folder, run the app.py file.  It will run on localhost:5000.
```
python3 app.py
```
