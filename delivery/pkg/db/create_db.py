# -*- coding: utf-8 -*-
from delivery.pkg.db import meta, model


def create_db():
    meta.create_all()

    session = meta.session

    msk = model.Destination(addr='Moscow')
    london = model.Destination(addr='London')
    session.add(msk)
    session.add(london)

    orders = [
        model.Order(destination=msk, user_id=1),
        model.Order(destination=msk, user_id=1),
        model.Order(destination=london, user_id=2),
    ]

    for order in orders:
        session.add(order)

    lots = [
        model.Lot(order=orders[0], product_id=1, count=1),
        model.Lot(order=orders[1], product_id=2, count=1),
        *[
            model.Lot(order=orders[2], product_id=i, count=2)
            for i in range(1, 15)
        ],
    ]

    for lot in lots:
        session.add(lot)

    session.commit()
