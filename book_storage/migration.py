# -*- coding: utf-8 -*-
from book_storage.application import create_application
from book_storage.pkg import db


def migrate():
    create_application()
    db.create_db()
