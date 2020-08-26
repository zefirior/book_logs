# -*- coding: utf-8 -*-
import logging
import logging.config

from flask import Flask, jsonify
from flask_log_request_id import RequestID

from delivery.pkg import db
from delivery.pkg.db import model
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

    @app.route('/ping', methods=['GET'])
    def ping():
        return 'pong'

    @app.route('/user/<int:user_id>/orders', methods=['GET'])
    def get_order(user_id):
        logger.info('got_request', extra={'endpoint': '/user/<int:user_id>/orders'})
        orders = model.Order.query.filter_by(user_id=user_id).all()
        orders = marshall_order(orders)

        return jsonify({'result': {'orders': orders}})

    return app


def marshall_order(orders):
    return {
        order.id: {
            'user_id': order.user_id,
            'destination': {
                'addr': order.destination.addr,
            },
            'lots': [{
                'id': lot.id,
                'count': lot.count,
                'product_id': lot.product_id,
            } for lot in order.lots],
        } for order in orders
    }
