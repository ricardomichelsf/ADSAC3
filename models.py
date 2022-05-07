# models.py


import datetime
from app import db


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __init__(self, name, categoria, preco):
        self. name = name
        self.categoria = categoria
        self.preco = preco