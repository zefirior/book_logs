# -*- coding: utf-8 -*-
from book_storage.pkg.db import meta, model


def create_db():
    meta.create_all()

    session = meta.session

    for i in range(1, 16):
        author = model.Author(id=i, name=f'Rudolf {i}')
        book = model.Book(id=i, title=f'{i} adventure', author=author)
        session.add(book)
        session.add(author)

    session.commit()
