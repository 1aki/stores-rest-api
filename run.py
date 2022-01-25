from app import app
from db import db

db.init_app(app)

# creates the tables. replacing create_tables.py
@app.before_first_request
def create_tables():
    db.create_all()