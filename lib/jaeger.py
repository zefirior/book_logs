# -*- coding: utf-8 -*-
import flask_opentracing
import jaeger_client
from opentracing_instrumentation.client_hooks import install_all_patches

from lib import settings


def init_jaeger(app):
    config = jaeger_client.Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'logging': True,
            'local_agent': {'reporting_host': settings.JAEGER_HOST}
        },
        service_name='books'
    )
    jaeger_tracer = config.initialize_tracer()
    flask_opentracing.FlaskTracing(jaeger_tracer, app=app)
    install_all_patches()
