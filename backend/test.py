from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from model import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse/temp.db'
db = SQLAlchemy(app)

db.create_all()
db.session.commit()
