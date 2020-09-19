from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/payments_dobrobot'
engine = create_engine("postgresql+psycopg2://dobrobot:dobrobot@/payments_dobrobot")

db = SQLAlchemy(app)
