# -*- coding: utf-8 -*-
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from lib import settings


def init_sentry():
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=[FlaskIntegration()]
    )
