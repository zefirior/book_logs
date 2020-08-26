# -*- coding: utf-8 -*-
import logging
import logging.config

from flask import Flask, request, jsonify
from flask_log_request_id import RequestID

from book_storage.pkg import db
from book_storage.pkg.db import model
from lib import settings
from lib.db import init_db
from lib.jaeger import init_jaeger
from lib.sentry import init_sentry

logger = logging.getLogger('app')


def create_application() -> Flask:
    logging.config.dictConfig(settings.create_logging_setting())

    app = Flask(__name__)
    init_sentry()
    init_db(app, db.meta)
    init_jaeger(app)
    RequestID(app)

    @app.route('/books', methods=['GET'])
    def book():
        logger.info('got_request', extra={'endpoint': '/books'})
        book_ids = request.args.getlist('book_ids', int)
        books = model.Book.query.filter(model.Book.id.in_(book_ids)).all()

        result = {}
        for b in books:
            result[b.id] = {
                'title': b.title,
                'author_name': b.author.name,
            }

        return jsonify({'result': result})

    @app.route('/ping', methods=['GET'])
    def ping():
        return 'pong'

    return app
