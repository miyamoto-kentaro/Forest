# model-exam/app.py
import os
from flask import Flask

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__name__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://miya:miyamoto1001@postgres:5432/ForestDB'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
if os.environ.get('DATABASE_URL') is None:
    database_uri = "sqlite:///data.db"
else:
    database_uri = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
