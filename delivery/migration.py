# -*- coding: utf-8 -*-
from delivery.application import create_application
from delivery.pkg import db


def migrate():
    create_application()
    db.create_db()
