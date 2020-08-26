# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

meta = SQLAlchemy()


class Author(meta.Model):
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(80), nullable=False)

    def __repr__(self):
        return f'<Author {self.name}>'


class Book(meta.Model):
    id = meta.Column(meta.Integer, primary_key=True)
    title = meta.Column(meta.String(255), nullable=False)
    author_id = meta.Column(meta.Integer, meta.ForeignKey(Author.id), nullable=False)

    author = relationship('Author', backref='books')

    def __repr__(self):
        return f'<Author {self.name}>'
