# -*- coding: utf-8 -*-
import os

JAEGER_HOST = 'jaeger'

SENTRY_DSN = '<your sentry dsn>'

DB_ADDR = os.environ['DB_ADDR']
DB_USER = os.environ['DB_USER']
DB_NAME = os.environ['DB_NAME']


def create_logging_setting():
    logging_dict = {
        'version': 1,
        'root': {
            'handlers': ['common'],
            'level': 'INFO',
        },
        'formatters': {
            'verbose': {
                '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
                'format': '%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d %(message)s %(request_id)s',
            },
        },
        'filters': {
            'request_id': {
                '()': 'flask_log_request_id.RequestIDLogFilter',
            },
        },

        'handlers': {
            'common': {
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'filters': ['request_id'],
                'level': 'INFO',
            },
        },

        'loggers': {
            'app': {
                'handlers': ['common'],
                'level': 'INFO',
                'propagate': False,
            }
        },
    }
    return logging_dict
