# -*- coding: utf-8 -*-
import os

target = os.environ['ENTRYPOINT_TARGET']

if target == 'book_storage':
    from book_storage.application import create_application
    app = create_application()
    app.run('0.0.0.0', 80)

elif target == 'migrate_book_storage':
    from book_storage.migration import migrate
    migrate()

elif target == 'delivery':
    from delivery.application import create_application
    app = create_application()
    app.run('0.0.0.0', 80)

elif target == 'migrate_delivery':
    from delivery.migration import migrate
    migrate()

elif target == 'cabinet':
    from cabinet.application import create_application
    app = create_application()
    app.run('0.0.0.0', 80)
