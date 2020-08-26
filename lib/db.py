# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from lib import settings


def database_uri(settings):
    return f'postgresql+psycopg2://{settings.DB_USER}:password@{settings.DB_ADDR}/{settings.DB_NAME}'


def init_db(app: Flask, db: SQLAlchemy):
    db.app = app
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri(settings)
    db.init_app(app)
