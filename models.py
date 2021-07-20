from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

db = SQLAlchemy(app)
Migrate(app, db)
# Main Colums


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer)
    seller_url = db.Column(db.Text)
    companies = db.Column(db.Text)
    evaluation_value = db.Column(db.Float)
    search_key = db.Column(db.Text)

    def __init__(self, name, price, seller_url, companies, evaluation_value, search_key, *args):
        # super(Person, self).__init__(*args))
        self.name = name
        self.price = price
        self.seller_url = seller_url
        self.companies = companies
        self.evaluation_value = evaluation_value
        self.search_key = search_key

    def __str__(self):
        return f"id = {self.id}, name = {self.name}"
