# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

meta = SQLAlchemy()


class Destination(meta.Model):
    id = meta.Column(meta.Integer, primary_key=True)
    addr = meta.Column(meta.String, nullable=False)


class Order(meta.Model):
    id = meta.Column(meta.Integer, primary_key=True)
    user_id = meta.Column(meta.Integer, nullable=False)
    destination_id = meta.Column(meta.Integer, meta.ForeignKey(Destination.id), nullable=False)

    lots = meta.relationship('Lot', backref='order', lazy='joined')
    destination = meta.relationship(Destination, lazy='joined')


class Lot(meta.Model):
    id = meta.Column(meta.Integer, primary_key=True)
    order_id = meta.Column(meta.Integer, meta.ForeignKey(Order.id), nullable=False)
    product_id = meta.Column(meta.Integer, nullable=False)
    count = meta.Column(meta.Integer, nullable=False)
