# -*- coding: utf-8 -*-
import logging
import logging.config

import requests
from flask import Flask, jsonify
from flask_log_request_id import RequestID, current_request_id

from lib import settings
from lib.jaeger import init_jaeger
from lib.sentry import init_sentry

logger = logging.getLogger('app')

ORDERS_URL = 'http://delivery/user/{user_id}/orders'
BOOKS_URL = 'http://book_storage/books'


def create_application() -> Flask:
    logging.config.dictConfig(settings.create_logging_setting())

    app = Flask(__name__)
    init_sentry()
    init_jaeger(app)
    RequestID(app)

    @app.route('/user/<int:user_id>/orders', methods=['GET'])
    def get_orders(user_id):
        logger.info('got_request', extra={'endpoint': '/user/<user_id>/orders'})

        headers = {'X-Request-ID': current_request_id()}

        response = requests.get(ORDERS_URL.format(user_id=user_id), headers=headers)
        orders = response.json()['result']['orders']

        book_ids = get_book_ids_from_orders(orders)
        response = requests.get(BOOKS_URL, params={'book_ids': book_ids}, headers=headers)
        books = response.json()['result']

        return jsonify({'result': {
            'orders': orders,
            'books': books,
        }})

    @app.route('/ping', methods=['GET'])
    def ping():
        logger.info('got_request', extra={'endpoint': '/ping'})
        return 'pong'

    return app


def get_book_ids_from_orders(orders):
    product_ids = set()
    for order in orders.values():
        for lot in order['lots']:
            product_ids.add(lot['product_id'])
    return list(product_ids)
